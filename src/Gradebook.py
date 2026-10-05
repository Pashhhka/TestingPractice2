class Gradebook:
    def __init__(self):
        self.students = {}

    def add_student(self, name: str):
        if name in self.students:
            raise ValueError("Студент уже существует")
        self.students[name] = []

    def add_grade(self, name: str, grade: int):
        if name not in self.students:
            raise KeyError("Студент не найден")
        if not (1 <= grade <= 5):
            raise ValueError("Оценка должна быть от 1 до 5")
        self.students[name].append(grade)

    # def get_student_average(self, name: str) -> float:
    #     if name not in self.students:
    #         raise KeyError("Студент не найден")
    #     grades = self.students[name]
    #     # БАГ: Если список оценок пуст, len(grades) равно 0. Произойдет деление на ноль.
    #     # Правильно: возвращать 0.0 или None, если оценок нет.
    #     return sum(grades) / len(grades)

    def get_student_average(self, name: str) -> float:
        if name not in self.students:
            raise KeyError("Студент не найден")
        grades = self.students[name]
        # ИСПРАВЛЕНО: Проверка на пустой список оценок для предотвращения деления на ноль
        if not grades:
            return 0.0
        return sum(grades) / len(grades)

    def get_excellent_students(self) -> list:
        # Студенты со средним баллом >= 4.5
        excellent = []
        for name, grades in self.students.items():
            if grades and (sum(grades) / len(grades)) >= 4.5:
                excellent.append(name)
        return excellent

    def remove_student(self, name: str):
        if name in self.students:
            del self.students[name]