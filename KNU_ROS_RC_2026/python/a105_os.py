import os


def main():
    print(f"운영체제: {os.name}")
    print(f"현재 위치: {os.getcwd()}")
    print(f"현재 위치: {os.listdir()}")
    folders = [name for name in os.listdir() if os.path.isdir(name)]
    print(folders)
    print(os.system("ls -al"))
    print(os.system("python3 a25_dictionary.py"))


if __name__ == "__main__":
    main()
