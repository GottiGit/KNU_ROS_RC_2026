from collections.abc import Iterable


class SimpleIter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


def main():
    iter = SimpleIter(0, 10)
    print(isinstance(iter, Iterable))
    print(isinstance("aa", str))
    print(isinstance("aa", object))
    for v in iter:
        print(v)


if __name__ == "__main__":
    main()
