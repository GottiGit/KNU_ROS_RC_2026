"""
main.py
-------
RC카 제어 UI 실행 진입점.

실행:
    uv run main.py
"""

from pathlib import Path

import webview
from KNU_ROS_RC_2026.rc_car_ui.backend.server import RcCarApiServer

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR / "frontend"


def main() -> None:
    server = RcCarApiServer(FRONTEND_DIR)
    server.start()

    try:
        webview.create_window(
            "RC Car Control",
            url=server.base_url,
            width=480,
            height=720,
            resizable=True,
        )
        webview.start()
    finally:
        server.stop()


if __name__ == "__main__":
    main()