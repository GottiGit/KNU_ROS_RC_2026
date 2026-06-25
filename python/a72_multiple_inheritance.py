class Person:
    def __init__(self, b):
        self.b = b

    def greeting(self):
        print("안녕하세요")


class University:
    def __init__(self, a):
        self.a = a

    def massage_credit(self):
        print("학점 관리")


class Undergraduate(Person, University):
    def __init__(self, c):
        Person.__init__(self, 2)
        University.__init__(self, 1)
        self.c = c


def main():
    choi = Undergraduate(3)
    print(choi.a, choi.b, choi.c)
    choi.greeting()
    choi.massage_credit()
    print(Undergraduate.__mro__)


if __name__ == "__main__":
    main()
