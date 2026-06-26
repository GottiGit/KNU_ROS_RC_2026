# sudo apt update
# sudo apt install -y \
#   pkg-config \
#   python3-gi \
#   python3-gi-cairo \
#   gir1.2-gtk-3.0 \
#   gir1.2-webkit2-4.1

# uv add "pywebview[gtk]"
import webview


def main():
    webview.create_window("hello", html="<h1>hello pywebview</h1>")
    webview.start()


if __name__ == "__main__":
    main()
