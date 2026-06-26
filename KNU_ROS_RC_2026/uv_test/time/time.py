
import datetime
from pathlib import Path

import webview

BASE_PATH = Path(__file__).resolve().parent
NOTE_PATH = BASE_PATH / "note.txt"
WEEKDAYS = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]


class TimeApi:
    def __init__(self):
        pass

    def getClockPayload(self):
        now = datetime.datetime.now()
        return {"time": now.strftime("%H:%M:%S"),
                "date": f"{now.year} 년 {now.month} 월{now.year} 일 {WEEKDAYS[now.weekday()]}"}


def main():
    webview.create_window(
        "탁상시계",
        url=(BASE_PATH / "front" / "text.html").as_uri(),
        js_api=TimeApi(),
        width=640,
        height=320,
        resizable=True
        )
    webview.start()


if __name__ == "__main__":
    main()