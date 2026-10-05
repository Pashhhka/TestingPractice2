class Library:
    def __init__(self):
        self.available_books = []
        self.borrowed_books = []

    def add_book(self, title: str):
        self.available_books.append(title)

    def borrow_book(self, title: str):
        if title not in self.available_books:
            raise ValueError("Книга недоступна или не существует")
        self.available_books.remove(title)
        self.borrowed_books.append(title)

    # def return_book(self, title: str):
    #     # БАГ: Нет проверки, находится ли книга в self.borrowed_books.
    #     # Можно передать любое название, и оно добавится в available_books.
    #     if title in self.borrowed_books:
    #         self.borrowed_books.remove(title)
    #     self.available_books.append(title)
    def return_book(self, title: str):
        # ИСПРАВЛЕНО: Добавлена проверка на наличие книги в списке выданных
        if title not in self.borrowed_books:
            raise ValueError("Книга не числится как выданная")
        self.borrowed_books.remove(title)
        self.available_books.append(title)

    def is_book_available(self, title: str) -> bool:
        return title in self.available_books

    def get_total_books(self) -> int:
        return len(self.available_books) + len(self.borrowed_books)