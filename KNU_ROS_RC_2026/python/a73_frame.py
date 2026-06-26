# __file__, __pacakage__,
# C 언어 에서 동작 할 수 있게 해주는 정보들..
import sys

print(sys._getframe().f_code)
print(sys._getframe().f_locals)
print(sys._getframe().f_globals)


def main():
    a = 1
    print(sys._getframe().f_code)
    print(sys._getframe().f_locals)


main()

# 함수 동작 할때 , 파이썬 프로그램 시작
