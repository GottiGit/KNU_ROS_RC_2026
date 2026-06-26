def main():
    number = int(input("정수를 입력하세요> "))

    # if number % 2:  # 0 1 -> 0 이면 false
    #     print("홀수 입니다.")
    # else:
    #     print("짝수 입니다.")
    print("홀수" if number % 2 else "짝수", "입니다.")


if __name__ == "__main__":
    main()
