"""
hardware.py
-----------
실제 RC카 하드웨어(모터 제어, 센서 읽기)에 대한 인터페이스.
지금은 mock(가짜) 구현만 있음 — 실제 하드웨어 연동 시 이 파일의
내용만 교체하면 서버/프론트엔드 코드는 그대로 사용 가능.

향후 실제 구현 시 예상되는 방식 (참고용 주석):
- GPIO 직접 제어 (라즈베리파이 등): RPi.GPIO 또는 gpiozero
- 시리얼 통신 (Arduino 등): pyserial로 USB 포트에 명령 전송
- ROS 토픽 발행: rclpy로 /cmd_vel 등에 Twist 메시지 publish
"""

import random
import time
from dataclasses import dataclass, field
from threading import Lock


@dataclass
class CarState:
    direction: str = "stop"   # "forward" | "backward" | "left" | "right" | "stop"
    speed: int = 0            # 0 ~ 100
    timestamp: float = field(default_factory=time.time)


class MockCarController:
    """
    실제 하드웨어 대신 동작하는 더미 컨트롤러.
    명령을 받으면 내부 상태만 갱신하고, 센서값은 랜덤하게 생성한다.
    """

    def __init__(self) -> None:
        self._lock = Lock()
        self._state = CarState()

    # ------------------------------------------------------------------
    # 주행 제어
    # ------------------------------------------------------------------
    def set_direction(self, direction: str) -> CarState:
        valid = {"forward", "backward", "left", "right", "stop"}
        if direction not in valid:
            raise ValueError(f"invalid direction: {direction}")
        with self._lock:
            self._state.direction = direction
            self._state.timestamp = time.time()
            return self._state

    def set_speed(self, speed: int) -> CarState:
        speed = max(0, min(100, int(speed)))
        with self._lock:
            self._state.speed = speed
            self._state.timestamp = time.time()
            return self._state

    def stop(self) -> CarState:
        with self._lock:
            self._state.direction = "stop"
            self._state.speed = 0
            self._state.timestamp = time.time()
            return self._state

    def get_state(self) -> CarState:
        with self._lock:
            return self._state

    # ------------------------------------------------------------------
    # 센서 (mock: 의미 없는 랜덤 값)
    # ------------------------------------------------------------------
    def read_sensors(self) -> dict:
        """
        실제 구현에서는 초음파/IR 거리센서, 배터리 전압, IMU 등을
        읽어와서 반환하게 됨. 지금은 랜덤 값으로 대체.
        """
        return {
            "distance_cm": round(random.uniform(5, 200), 1),
            "battery_pct": round(random.uniform(20, 100), 1),
            "imu_yaw_deg": round(random.uniform(-180, 180), 1),
            "timestamp": time.time(),
        }


# 싱글톤 인스턴스 — 서버 전체에서 하나의 차량 상태를 공유
car_controller = MockCarController()