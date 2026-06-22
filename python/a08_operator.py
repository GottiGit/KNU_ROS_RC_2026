class Add_test:
    def __add__(self, other):
        return "더하기 연산이 실행 되었다"


def main():
    print(2 ** 4)
    print(2 ** 64)
    print(18/4)
    print(type(18/3))

    print(18 // 3)
    print(type(18 // 3))

    print(14 % 3)
    a = Add_test()
    b = Add_test()
    print(a + b)


if __name__ == "__main__":
    main()
