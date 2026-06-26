class Mylist:
    def __init__(self):
        self.myVariable = "choi"    # 인스턴스 변수
        self.myVariable2 = "su"     # ...
        self.myList = list()

    def append(self, ele):          # 메소드
        self.myList.append(ele)


def main():
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    print(list_a + list_b)
    print(list_a)
    list_a.extend(list_b)
    print(list_a)

    list_b.append(7)
    list_b.append(8)
    print(list_b)
    list_b.insert(1, 4.5)   # type: ignore
    print(list_b)
    myList_a = Mylist()
    myList_a.append("choi su gil")
    print(myList_a.myVariable, myList_a.myVariable2, myList_a.myList)


if __name__ == "__main__":
    main()
