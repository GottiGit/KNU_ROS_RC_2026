from pathlib import Path


def main():
    url = Path(__file__).parent.parent / "data" / "text.txt"
    bin_url = Path(__file__).parent.parent / "data" / "text.bin"
    with open(url, "r", encoding='utf-8') as f:
        data = f.read()
        print(data)
        f.seek(0)
        while data := f.readline():
            print(data)
        f.seek(0)
        data = f.readlines()
        print(data)
    binary_data = b'\1\2\3'
    with open(bin_url, "wb") as f:
        f.write(binary_data)
    with open(bin_url, "rb") as f:
        data = f.read()
        print(data)


if __name__ == "__main__":
    main()
