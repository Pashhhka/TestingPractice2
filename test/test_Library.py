import pytest
from mutation_src.Library import Library

def test_add_and_availability():
    lib = Library()
    lib.add_book("1984")
    assert lib.is_book_available("1984") is True
    assert lib.get_total_books() == 1

def test_borrow_book():
    lib = Library()
    lib.add_book("Мастер и Маргарита")
    lib.borrow_book("Мастер и Маргарита")

    assert lib.is_book_available("Мастер и Маргарита") is False
    assert lib.get_total_books() == 1  # Книга все еще числится в библиотеке (выдана)

def test_borrow_unavailable_book():
    lib = Library()
    with pytest.raises(ValueError):
        lib.borrow_book("Неизвестная книга")

def test_return_book():
    lib = Library()
    lib.add_book("Гарри Поттер")
    lib.borrow_book("Гарри Поттер")
    lib.return_book("Гарри Поттер")

    assert lib.is_book_available("Гарри Поттер") is True

# ИСПРАВЛЕНО: Уточнено сообщение ошибки для уничтожения M3
def test_return_unborrowed_book():
    lib = Library()
    lib.add_book("Властелин колец")
    with pytest.raises(ValueError, match="Книга не числится как выданная"):
        lib.return_book("Властелин колец")
    assert lib.get_total_books() == 1