import datetime


def main():
    ptime = datetime.datetime.now()
    list_a = [0, 1, 2, 3, 4, 5, 6]
    list_b = ["a", "b", "c", "d", "e", "f", ptime]
    del list_a[0]   # 객체를 지우는 키워드
    del list_b[2]
    del list_b[5]   # 객체를 메모리에서 지우고 싶으면 리스트와 객체 둘다 지워야 한다.
    del ptime
    print(list_a)
    print(list_b)
    # print(ptime)
    # del list_a      # heap 에 있는 메모리 공간이 삭제 됨
    # print(list_a)

    print(list_b.pop())
    print(list_b)

    if "a" in list_b:
        list_b.remove("a")
    print(list_b)


if __name__ == "__main__":
    main()
