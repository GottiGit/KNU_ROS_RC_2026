def print_n_times(value, n=2, v=3, g=5, *sum):
    sum_ = 0
    for i in range(n):
        print(value)
    for i in sum:
        sum_ += i
    return sum_


def main():
    print(print_n_times("안녕하세요"))      # positonal, default, 가변인자
    # 가변인자가 없으면, default 인자 or keyward 인자


if __name__ == "__main__":
    main()
