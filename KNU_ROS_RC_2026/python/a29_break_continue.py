import random


def main():
    li = [random.randint(0, 100) for _ in range(100)]
    print(li)
    for number in li:
        if number < 50:
            continue
        print(number, ", ", end="")
        if number > 80:
            break
    print()


if __name__ == "__main__":
    main()
