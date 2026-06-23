# sudo apt update
# sudo apt install python3-pip
# pip install pywebview
from pathlib import Path

import webview

BASE_PATH = Path(__file__).resolve().parent
NOTE_PATH = BASE_PATH / "note.txt"


class MemoApi:
    def __init__(self):
        pass

    def save_note(self, text):
        NOTE_PATH.write_text(text, encoding="utf-8")
        return {"status": "saved", "path": str(NOTE_PATH)}

    def load_note(self):
        return {"text": NOTE_PATH.read_text(encoding="utf-8")}


def main():
    webview.create_window(
        "simple text",
        url=(BASE_PATH / "text.html").as_uri(),
        js_api=MemoApi(),
        width=640,
        height=520,
        resizable=True
        )
    webview.start()


if __name__ == "__main__":
    main()