import pytest
from mutation_src.Gradebook import Gradebook

def test_add_student():
    gb = Gradebook()
    gb.add_student("Иван")
    assert "Иван" in gb.students


def test_add_duplicate_student():
    gb = Gradebook()
    gb.add_student("Анна")
    with pytest.raises(ValueError):
        gb.add_student("Анна")


def test_add_grade():
    gb = Gradebook()
    gb.add_student("Олег")
    gb.add_grade("Олег", 5)
    gb.add_grade("Олег", 4)
    assert gb.get_student_average("Олег") == 4.5


def test_add_invalid_grade():
    gb = Gradebook()
    gb.add_student("Мария")
    with pytest.raises(ValueError):
        gb.add_grade("Мария", 6)


# ДОБАВЛЕНО: Проверка нижней границы оценок для уничтожения M2
def test_add_grade_below_minimum():
    gb = Gradebook()
    gb.add_student("Мария")
    with pytest.raises(ValueError):
        gb.add_grade("Мария", 0)


# ДОБАВЛЕНО: Проверка получения среднего балла отсутствующего студента для уничтожения M3
def test_get_average_nonexistent_student():
    gb = Gradebook()
    with pytest.raises(KeyError):
        gb.get_student_average("Неизвестный")


# ИСПРАВЛЕНО: Добавлен студент со средним баллом 4.25 для уничтожения M4
def test_excellent_students():
    gb = Gradebook()
    gb.add_student("Иван")
    gb.add_grade("Иван", 5)
    gb.add_grade("Иван", 4)  # Среднее 4.5

    gb.add_student("Олег")
    gb.add_grade("Олег", 3)  # Среднее 3.0

    gb.add_student("Павел")
    gb.add_grade("Павел", 5)
    gb.add_grade("Павел", 4)
    gb.add_grade("Павел", 4)
    gb.add_grade("Павел", 4)  # Среднее 4.25 (при M4 попадает в отличники и убьет мутанта)

    excellent = gb.get_excellent_students()
    assert "Иван" in excellent
    assert "Олег" not in excellent
    assert "Павел" not in excellent


def test_average_without_grades():
    gb = Gradebook()
    gb.add_student("Петр")
    assert gb.get_student_average("Петр") == 0.0


def test_remove_student():
    gb = Gradebook()
    gb.add_student("Анна")
    gb.remove_student("Анна")
    assert "Анна" not in gb.students