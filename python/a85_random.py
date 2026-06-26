import random


def main():
    hanguls = list("최강박이손정적고구류오김송곽유")
    hanguls2 = list("가나다라마바사아자차카파타하길진재형준석화섭윤진혁시동상")
    for _ in range(100):
        name = random.choice(hanguls) + str().join(random.choices(hanguls2, k=2))
        print(name)

    mu = 3
    sigma = 5
    print(random.gauss(mu, sigma))
    print(random.normalvariate(mu, sigma))


if __name__ == "__main__":
    main()
