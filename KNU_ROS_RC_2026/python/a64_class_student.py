from pathlib import Path


class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self. math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def to_string(self):
        print(f"{self.name}\t{self.get_sum()}\t{self.get_average()}")


def main():
    student_path = Path(__file__).parent.parent / "data/student_info.data"
    students = []
    with open(student_path, "r", encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            name, korean, math, english, science = line.split()

            student = Student(name, int(korean), int(math), int(english), int(science))
            students.append(student)

    print("이름\t총점\t평균")
    for student in students:
        student.to_string()


if __name__ == "__main__":
    main()
