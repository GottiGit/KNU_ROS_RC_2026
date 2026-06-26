def main():
    print(10 == 100)    # False
    print(10 != 100)    # True
    print(10 < 100)     # True
    print(100 <= 100)   # True
    print(type(True))

    print(not True)         # False
    print(not False)        # True
    print(True and True)    # True
    print(False or False)   # False

    a = int(input("100 보다 큰 숫자를 넣으세요>"))

    if a > 100:
        print("a는 100 보다 큽니다.")
    print("프로그램을 종료 합니다.")


if __name__ == "__main__":
    main()
