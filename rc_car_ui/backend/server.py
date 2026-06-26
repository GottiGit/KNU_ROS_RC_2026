"""
server.py
---------
RC카 제어용 Flask 서버.

엔드포인트:
- GET  /                       프론트엔드 index.html 서빙
- GET  /api/state               현재 차량 상태(방향/속도) 조회
- POST /api/control/direction    방향 설정  {"direction": "forward"}
- POST /api/control/speed        속도 설정  {"speed": 50}
- POST /api/control/stop          정지
- GET  /api/state/events         차량 상태 SSE 스트림 (여러 창 동기화용)
- GET  /api/sensors               센서값 단발 조회
- GET  /api/sensors/events        센서값 SSE 스트림 (주기적 push)
"""

import json
import queue
import time
from dataclasses import asdict
from pathlib import Path
from threading import Lock, Thread
from urllib import error, request

from flask import Flask, Response, jsonify, request as flask_request, send_from_directory
from werkzeug.serving import BaseWSGIServer, make_server

from .hardware import car_controller

RC_CAR_PORT = 49500
SENSOR_PUSH_INTERVAL_SEC = 1.0

type StateEventQueue = "queue.Queue[dict]"


class RcCarApiServer:
    def __init__(self, frontend_dir: Path) -> None:
        self.frontend_dir = Path(frontend_dir).resolve()
        self.port = RC_CAR_PORT

        self._lock = Lock()
        self._state_clients: list[queue.Queue] = []
        self._sensor_clients: list[queue.Queue] = []

        self._server: BaseWSGIServer | None = None
        self._thread: Thread | None = None
        self._sensor_thread: Thread | None = None
        self._owns_server = False
        self._running = False

        self.app = Flask(__name__, static_folder=str(self.frontend_dir), static_url_path="")
        self._register_routes()

    # ------------------------------------------------------------------
    # 라우트 등록
    # ------------------------------------------------------------------
    def _register_routes(self) -> None:
        self.app.add_url_rule("/", "index", self._serve_index)

        self.app.add_url_rule("/api/state", "get_state", self._get_state)
        self.app.add_url_rule(
            "/api/control/direction", "set_direction", self._set_direction, methods=["POST"]
        )
        self.app.add_url_rule(
            "/api/control/speed", "set_speed", self._set_speed, methods=["POST"]
        )
        self.app.add_url_rule(
            "/api/control/stop", "stop", self._stop, methods=["POST"]
        )
        self.app.add_url_rule("/api/state/events", "state_events", self._stream_state_events)

        self.app.add_url_rule("/api/sensors", "get_sensors", self._get_sensors)
        self.app.add_url_rule("/api/sensors/events", "sensor_events", self._stream_sensor_events)

    def _serve_index(self):
        return send_from_directory(self.frontend_dir, "index.html")

    # ------------------------------------------------------------------
    # 주행 제어 핸들러
    # ------------------------------------------------------------------
    def _get_state(self):
        return jsonify(asdict(car_controller.get_state()))

    def _set_direction(self):
        body = flask_request.get_json(silent=True) or {}
        direction = body.get("direction", "stop")
        try:
            state = car_controller.set_direction(direction)
        except ValueError as exc:
            return jsonify({"error": str(exc)}), 400
        payload = asdict(state)
        self._broadcast(self._state_clients, payload)
        return jsonify(payload)

    def _set_speed(self):
        body = flask_request.get_json(silent=True) or {}
        speed = body.get("speed", 0)
        state = car_controller.set_speed(speed)
        payload = asdict(state)
        self._broadcast(self._state_clients, payload)
        return jsonify(payload)

    def _stop(self):
        state = car_controller.stop()
        payload = asdict(state)
        self._broadcast(self._state_clients, payload)
        return jsonify(payload)

    def _stream_state_events(self) -> Response:
        return self._sse_stream(self._state_clients, asdict(car_controller.get_state()))

    # ------------------------------------------------------------------
    # 센서 핸들러
    # ------------------------------------------------------------------
    def _get_sensors(self):
        return jsonify(car_controller.read_sensors())

    def _stream_sensor_events(self) -> Response:
        return self._sse_stream(self._sensor_clients, car_controller.read_sensors())

    # ------------------------------------------------------------------
    # 공용 SSE 유틸
    # ------------------------------------------------------------------
    def _broadcast(self, clients: list[queue.Queue], payload: dict) -> None:
        for client_queue in list(clients):
            client_queue.put(payload)

    def _sse_stream(self, clients: list[queue.Queue], initial_payload: dict) -> Response:
        client_queue: queue.Queue = queue.Queue()
        with self._lock:
            clients.append(client_queue)
            client_queue.put(initial_payload)

        def event_stream():
            try:
                while True:
                    payload = client_queue.get()
                    yield f"data: {json.dumps(payload)}\n\n"
            finally:
                with self._lock:
                    if client_queue in clients:
                        clients.remove(client_queue)

        return Response(event_stream(), mimetype="text/event-stream")

    # ------------------------------------------------------------------
    # 센서 주기적 push (백그라운드 스레드)
    # ------------------------------------------------------------------
    def _sensor_push_loop(self) -> None:
        while self._running:
            payload = car_controller.read_sensors()
            self._broadcast(self._sensor_clients, payload)
            time.sleep(SENSOR_PUSH_INTERVAL_SEC)

    # ------------------------------------------------------------------
    # 서버 생명주기
    # ------------------------------------------------------------------
    @property
    def base_url(self) -> str:
        return f"http://127.0.0.1:{self.port}"

    def _is_server_ready(self) -> bool:
        try:
            with request.urlopen(f"{self.base_url}/api/state", timeout=1) as resp:
                return resp.status == 200
        except (OSError, error.URLError):
            return False

    def start(self) -> None:
        if self._is_server_ready():
            return

        try:
            self._server = make_server("127.0.0.1", self.port, self.app, threaded=True)
        except OSError as exc:
            if exc.errno in {10048, 98} and self._is_server_ready():
                return
            raise

        self._running = True
        self._thread = Thread(target=self._server.serve_forever, daemon=True)
        self._thread.start()

        self._sensor_thread = Thread(target=self._sensor_push_loop, daemon=True)
        self._sensor_thread.start()

        self._owns_server = True

    def stop(self) -> None:
        self._running = False
        if not self._owns_server or self._server is None or self._thread is None:
            return
        self._server.shutdown()
        self._thread.join(timeout=1)
        if self._sensor_thread is not None:
            self._sensor_thread.join(timeout=SENSOR_PUSH_INTERVAL_SEC + 1)