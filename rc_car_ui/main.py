"""
main.py
-------
RC카 제어 UI 실행 진입점.

실행:
    uv run main.py
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR / "frontend"

# 어느 위치(cwd)에서 실행하더라도 이 파일이 있는 폴더를 기준으로
# backend 패키지를 찾을 수 있도록 경로를 보장한다.
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

import webview  # noqa: E402
from backend.server import RcCarApiServer  # noqa: E402


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