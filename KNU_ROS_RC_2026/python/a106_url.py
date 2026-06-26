from urllib import request


def main():
    a = request.urlopen("https://google.com")
    print(a.read())
    # web scrapping 을 할 수 있다 하지만 번거롭다
    # 왠만하면 bs4 beautiful soup4 이거 쓰세요


if __name__ == "__main__":
    main()
