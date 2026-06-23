import datetime

from a01_hello import main as hello_main


def main():
    hello_main()
    now = datetime.datetime.now()

    if 9 < now.hour < 12:
        print(f"현재 시각은 {now.hour}로 오전 입니다.")
    elif now.hour < 9:
        print(f"현재 시각은 {now.hour}로 새벽 입니다.")
    else:
        print(f"현재 시각은 {now.hour}로 오후 입니다.")
    # now = now.replace(month=3) 숫자를 바꾸어서 테스트 해 보세요
    print(now.month, type(now.month))
    # 봄, 여름, 가을, 겨울 을 출력하세요
    # 12, 1, 2, 3 -> 겨울
    # 4, 5 -> 봄
    # 6, 7, 8 -> 여름
    # 9, 10, 11 -> 가을
    if now.month < 3:
        print(f"이번 달은 {now.month}로 겨울입니다.")
    elif now.month <= 5:
        print(f"이번 달은 {now.month}로 봄입니다.")
    elif now.month <= 8:
        print(f"이번 달은 {now.month}로 여름입니다.")
    elif now.month <= 11:
        print(f"이번 달은 {now.month}로 가을입니다.")
    else:
        print(f"이번 달은 {now.month}로 겨울입니다.")

    if now.month in [12, 1, 2, 3]:
        print("겨울")
    elif now.month in [4, 5]:
        print("봄")
    elif now.month in [6, 7, 8]:
        print("여름")
    elif now.month in [9, 10, 11]:
        print("가을")


if __name__ == "__main__":
    main()
