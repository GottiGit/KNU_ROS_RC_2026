import datetime
import math


class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_circumference(self):
        return 2 * math.pi * self.__radius

    def get_area(self):
        return math.pi * (self.__radius) ** 2

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if isinstance(value, int):
            self.__radius = value
        elif value < 0:
            raise ValueError
        else:
            raise ValueError

    @radius.getter
    def radius(self):
        print("변수 요청이 있었다")
        return self.__radius


class Rectangle(Circle):
    def __init__(self, radius):
        super().__init__(5)
        self.__radius = radius


def print_c(c):
    print("원의 둘레와 넓이를 구합니다")
    print(f"원의 둘레: {c.get_circumference():.2f}")
    print(f"원의 넓이: {c.get_area():.2f}")


def main():
    c = Circle(5)
    print(c.__dict__)
    print(c._Circle__radius)
    r = Rectangle(6)
    print(r.__dict__)
    # __변수는 overriding 을 방지하는 맹글링기능이다

    print_c(c)
    c.radius = 10
    print(c.radius)
    print_c(c)
    # 왜 프로퍼티를 쓰는가? -> 인스턴스 변수를 제어하려고


if __name__ == "__main__":
    main()
