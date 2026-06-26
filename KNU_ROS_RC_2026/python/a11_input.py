def main():
    input_var = input("숫자를 입력하세요>")
    print(type(input_var), input_var)
    # try:
    #     print(int(input_var) + 100)
    # except ValueError:
    #     print("숫자가 아닙니다")
    if input_var.isdigit():
        print(int(input_var) + 100)
    else:
        print("숫자가 아닙니다")


if __name__ == "__main__":
    main()
