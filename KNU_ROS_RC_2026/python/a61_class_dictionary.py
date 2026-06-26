import json
from pathlib import Path


def main():
    student_path = Path(__file__).parent.parent / "data/student_info.json"
    with open(student_path, "r", encoding='utf-8') as f:
        students = json.load(f)

    print("이름\t총점\t평균")
    for student in students:
        score_sum = (student["korean"] + student["math"] + student["english"] + student["science"])
        score_average = score_sum / 4
        print(f"{student['name']}\t{score_sum}\t{score_average}")


if __name__ == "__main__":
    main()
