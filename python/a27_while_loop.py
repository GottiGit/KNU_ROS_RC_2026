import time


def main():
    i = int()
    while i < 10:
        print(f"{i} 번째 실행 중...")
        i += 1
    try:
        while True:
            print('.', end="", flush=True)
            time.sleep(0.1)     # fps 설정 숫자를 계산
            # 블럭킹 코드를 추가(web  closer) - callback
    except KeyboardInterrupt:
        print("키보드 인터럽트!!")

    list_test = list("choi su gil is python teacher!!")
    print(list_test)
    while "s" in list_test:
        list_test.remove("s")
    print(list_test)


if __name__ == "__main__":
    main()
