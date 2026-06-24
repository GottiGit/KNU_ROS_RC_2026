from pathlib import Path


def main():
    # print(Path(__file__).parent)
    # f = open(Path(__file__).parent.parent / "data" / "text.txt", "w")
    # f.write("안녕하세요\n")
    # f.close()
    url = Path(__file__).parent.parent / "data" / "text.txt"
    with open(url, "a", encoding='utf-8') as f:
        f.write("안녕하세요\n")


if __name__ == "__main__":
    main()
