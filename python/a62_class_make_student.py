from pathlib import Path


def create_student(name, korean, math, english, science):
    return {
        "name": name,
        "korean": korean,
        "math": math,
        "english": english,
        "science": science
    }


def main():
    student_path = Path(__file__).parent.parent / "data/student_info.data"
    students = []
    with open(student_path, "r", encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            name, korean, math, english, science = line.split()

            student = create_student(name, int(korean), int(math), int(english), int(science))
            students.append(student)

    print("이름\t총점\t평균")
    for student in students:
        score_sum = (student["korean"] + student["math"] + student["english"] + student["science"])
        score_average = score_sum / 4
        print(f"{student['name']}\t{score_sum}\t{score_average}")


if __name__ == "__main__":
    main()
