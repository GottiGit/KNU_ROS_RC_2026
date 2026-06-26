# RC Car Control UI

Flask 백엔드 + pywebview 프론트엔드로 만든 RC카 제어 UI.
주행 제어, 속도 제어, 센서 데이터 표시를 담당.

하드웨어 연동은 아직 mock 상태 (backend/hardware.py 참고).

## Ubuntu 22.04 사전 준비 (GTK 백엔드)

pywebview[gtk]는 시스템 GTK/WebKit 패키지가 필요합니다.

```bash
sudo apt update
sudo apt install -y \
  pkg-config \
  python3-gi \
  python3-gi-cairo \
  gir1.2-gtk-3.0 \
  gir1.2-webkit2-4.1
```

## 실행

```bash
uv sync
uv run main.py
```

## 구조

```
rc_car_ui/
├── pyproject.toml       # uv 의존성: flask, pywebview[gtk]
├── main.py               # webview 실행 진입점, 서버 시작/종료 관리
├── backend/
│   ├── hardware.py        # 차량 제어/센서 인터페이스 (현재 mock)
│   └── server.py          # Flask 서버: REST API + SSE 스트리밍
└── frontend/
    ├── index.html          # 방향 패드, 속도 슬라이더, 센서 카드
    ├── app.js              # fetch()로 제어, EventSource로 상태/센서 수신
    └── style.css
```

## API

| Method | Path                      | 설명                          |
|--------|---------------------------|-------------------------------|
| GET    | `/api/state`               | 현재 방향/속도 조회             |
| POST   | `/api/control/direction`    | `{"direction": "forward"}`     |
| POST   | `/api/control/speed`        | `{"speed": 50}`                |
| POST   | `/api/control/stop`          | 정지                          |
| GET    | `/api/state/events`          | 방향/속도 변경 SSE (다중창 동기화) |
| GET    | `/api/sensors`               | 센서값 단발 조회                |
| GET    | `/api/sensors/events`        | 센서값 SSE (1초 간격 push)      |

## 실제 하드웨어 연동 시

`backend/hardware.py`의 `MockCarController`만 실제 구현으로 교체하면 됨.
서버(`server.py`)와 프론트엔드는 그대로 유지.

- GPIO 직접 제어: `RPi.GPIO` / `gpiozero`
- 시리얼(Arduino 등): `pyserial`로 USB 명령 전송
- ROS 토픽: `rclpy`로 `/cmd_vel` 등에 publish