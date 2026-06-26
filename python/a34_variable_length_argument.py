import random


def sum_all(a, b, c, *value):   # positional 다음에 가변 인자
    sum = 0
    print(type(value))
    print(a, b, c)
    for i in value:
        sum += i
    avr = sum/len(value)
    return sum, avr


def main():
    s, a = sum_all(100, 200, 300, 500, 123, 5234, 314)
    print(f"합계는 {s}, 평균은 {a}")

    list_a = [random.randint(0, 100) for _ in range(100)]
    s, a = sum_all(*list_a)     # (list_a[0], list_a[1], ...)
    print(f"합계는 {s}, 평균은 {a}")


if __name__ == "__main__":
    main()
