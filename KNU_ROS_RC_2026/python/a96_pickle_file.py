import pickle
import random
from pathlib import Path


def main():
    li = [random.randint(0, 100) for _ in range(1000)]
    pickle_path = Path(__file__).parent / "random_list.pickle"
    with pickle_path.open("wb") as f:
        pickle.dump(li, f)
    print("피클 파일이 생성되었습니다")


if __name__ == "__main__":
    main()
