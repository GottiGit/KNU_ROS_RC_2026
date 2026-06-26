def simple_rapper(func):
    def wrapper():
        print("func 실행 전 코드..")
        func()
        print("func 실행 후 코드..")
    return wrapper


@simple_rapper
def print_hello():
    print("print_hello 함수가 실행됨")


def main():
    # wrapper = simple_rapper(print_hello)
    # wrapper()
    # wrapper()
    # wrapper()
    print_hello()


if __name__ == "__main__":
    main()
