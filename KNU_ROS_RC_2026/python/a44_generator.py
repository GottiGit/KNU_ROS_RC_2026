def test():
    print("A함수가 호출 되었습니다")
    yield "re"
    print("B함수가 호출 되었습니다")
    yield "re"
    print("C함수가 호출 되었습니다")
    yield "re"


def main():
    ge = test()     # 함수의 실행이 매번 다른 결과를 요구할때
    print(ge)       # 일련의 과정이 결정되어서 연속적으로 일을 수행할때
    # print(ge.__next__())
    # print(next(ge))
    # print(next(ge))
    # print(next(ge))
    for re in ge:
        print(re)


if __name__ == "__main__":
    main()
