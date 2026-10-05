class Gradebook:
    def __init__(self):
        self.students = {}

    # MUT-GB-01
    def add_student(self, name: str):
        if name in self.students:
            raise ValueError("Студент уже существует")
        self.students[name] = []

    # def add_student(self, name: str):
    #     if name in self.students:
    #         # МУТАЦИЯ: замена ValueError на KeyError
    #         raise KeyError("Студент уже существует")
    #     self.students[name] = []

    # MUT-GB-02
    def add_grade(self, name: str, grade: int):
        if name not in self.students:
            raise KeyError("Студент не найден")
        if not (1 <= grade <= 5):
            raise ValueError("Оценка должна быть от 1 до 5")
        self.students[name].append(grade)

    # def add_grade(self, name: str, grade: int):
    #     if name not in self.students:
    #         raise KeyError("Студент не найден")
    #     # МУТАЦИЯ: нижняя граница разрешенных оценок расширена до 0
    #     if not (0 <= grade <= 5):
    #         raise ValueError("Оценка должна быть от 1 до 5")
    #     self.students[name].append(grade)

    # MUT-GB-03
    def get_student_average(self, name: str) -> float:
        if name not in self.students:
            raise KeyError("Студент не найден")
        grades = self.students[name]
        if not grades:
            return 0.0
        return sum(grades) / len(grades)

    # def get_student_average(self, name: str) -> float:
    #     if name not in self.students:
    #         # МУТАЦИЯ: замена KeyError на ValueError
    #         raise ValueError("Студент не найден")
    #     grades = self.students[name]
    #     if not grades:
    #         return 0.0
    #     return sum(grades) / len(grades)

    # MUT-GB-04
    # def get_excellent_students(self) -> list:
    #     excellent = []
    #     for name, grades in self.students.items():
    #         if grades and (sum(grades) / len(grades)) >= 4.5:
    #             excellent.append(name)
    #     return excellent

    def get_excellent_students(self) -> list:
        excellent = []
        for name, grades in self.students.items():
            # МУТАЦИЯ: критерий отличника снижен до > 4.0
            if grades and (sum(grades) / len(grades)) > 4.0:
                excellent.append(name)
        return excellent

    # MUT-GB-05
    def remove_student(self, name: str):
        if name in self.students:
            del self.students[name]

    # def remove_student(self, name: str):
    #     # МУТАЦИЯ: тело метода очищено (ничего не делает)
    #     pass