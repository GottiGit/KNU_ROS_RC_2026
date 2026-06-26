import math


class MinusError(Exception):
    def __init__(self):
        message = "음수는 허용되지 않습니다."
        super().__init__(message)


def main():
    user_input = input("양의 정수 입력: ")
    try:
        number_input = int(user_input)
        if number_input < 0:
            raise MinusError
    except MinusError as e:
        print(e)
    except ValueError as e:
        print(e)
    else:
        print(f"원의 반지름: {number_input}")
        print(f"원의 둘레: {number_input * 2 * math.pi}")
        print(f"원의 넓이: {math.pi * number_input**2}")
    finally:
        print("----- 프로그램이 종료 되었습니다 ----")


if __name__ == "__main__":
    main()
