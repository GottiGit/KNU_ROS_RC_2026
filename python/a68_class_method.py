from pathlib import Path


class Student:
    count = int()
    students = []

    def __init__(self, name, korean, math, english, science):
        # 인스턴스 변수는 init 에서 생성한다
        # (규칙이 아니지 왠만하면 여기서 만드시오)
        # init 은 생성할때 반드시 한번만 실행 됩니다
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        Student.students.append(self)
        print(f"{Student.count} 번째 학생이 생성 되었습니다.")

    def get_sum(self):
        self.sum = "합계입니다"
        return self.korean + self. math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    # 인스턴스변수를 하나씩 참조하지 않은상황, 클래스 변수를 써야만 되는상황
    @classmethod
    def print(cls):
        print(f"현재 생성된 총 학생수는 {cls.count} 입니다")
        print()
        print("---------------학생목록---------------")
        print("이름\t총점\t평균")
        for student in cls.students:
            print(student)
        print("--------------------------------------")

    def __str__(self):
        return f"{self.name}\t{self.get_sum()}\t{self.get_average()}"

    def __eq__(self, value):
        if isinstance(value, Student):
            return self.get_sum() == value.get_sum()
        else:
            raise ValueError

    def __ne__(self, value):
        if isinstance(value, Student):
            return self.get_sum() != value.get_sum()
        else:
            raise ValueError

    def __gt__(self, value):
        if isinstance(value, Student):
            return self.get_sum() > value.get_sum()
        else:
            raise ValueError

    def __ge__(self, value):
        if isinstance(value, Student):
            return self.get_sum() >= value.get_sum()
        else:
            raise ValueError

    def __lt__(self, value):
        if isinstance(value, Student):
            return self.get_sum() < value.get_sum()
        else:
            raise ValueError

    def __le__(self, value):
        if isinstance(value, Student):
            return self.get_sum() <= value.get_sum()
        else:
            raise ValueError


def load_student_data():
    student_path = Path(__file__).parent.parent / "data/student_info.data"
    with open(student_path, "r", encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            name, korean, math, english, science = line.split()

            Student(name, int(korean), int(math), int(english), int(science))


def main():
    load_student_data()
    Student.print()


if __name__ == "__main__":
    main()
