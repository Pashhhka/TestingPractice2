import pytest
from mutation_src.TaskManager import TaskManager


def test_add_task():
    tm = TaskManager()
    tm.add_task("Купить молоко")
    assert tm.get_total_tasks_count() == 1
    assert tm.get_pending_tasks()[0]["title"] == "Купить молоко"


def test_add_empty_task():
    tm = TaskManager()
    with pytest.raises(ValueError):
        tm.add_task("   ")  # Пустая строка должна вызывать ошибку


def test_complete_task():
    tm = TaskManager()
    tm.add_task("Задача 1")
    tm.complete_task("Задача 1")
    assert len(tm.get_completed_tasks()) == 1
    assert len(tm.get_pending_tasks()) == 0


def test_complete_unknown_task():
    tm = TaskManager()
    with pytest.raises(KeyError):
        tm.complete_task("Несуществующая задача")


def test_clear_completed():
    tm = TaskManager()
    tm.add_task("Задача 1")
    tm.add_task("Задача 2")
    tm.add_task("Задача 3")

    # Завершаем две задачи ПОДРЯД
    tm.complete_task("Задача 1")
    tm.complete_task("Задача 2")

    tm.clear_completed()
    assert tm.get_total_tasks_count() == 1