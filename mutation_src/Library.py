class Library:
    def __init__(self):
        self.available_books = []
        self.borrowed_books = []

    # MUT-LIB-01
    def add_book(self, title: str):
        self.available_books.append(title)

    # def add_book(self, title: str):
    #     # МУТАЦИЯ: к названию книги добавляется лишний пробел
    #     self.available_books.append(title + " ")

    # MUT-LIB-02
    def borrow_book(self, title: str):
        if title not in self.available_books:
            raise ValueError("Книга недоступна или не существует")
        self.available_books.remove(title)
        self.borrowed_books.append(title)

    # def borrow_book(self, title: str):
    #     # МУТАЦИЯ: убран not (инверсия условия проверки доступности)
    #     if title in self.available_books:
    #         raise ValueError("Книга недоступна или не существует")
    #     self.available_books.remove(title)
    #     self.borrowed_books.append(title)

    # MUT-LIB-03
    # def return_book(self, title: str):
    #     if title not in self.borrowed_books:
    #         raise ValueError("Книга не числится как выданная")
    #     self.borrowed_books.remove(title)
    #     self.available_books.append(title)

    def return_book(self, title: str):
        # МУТАЦИЯ: удалена проверка наличия книги в borrowed_books
        self.borrowed_books.remove(title)
        self.available_books.append(title)

    # MUT-LIB-04
    def is_book_available(self, title: str) -> bool:
        return title in self.available_books

    # def is_book_available(self, title: str) -> bool:
    #     # МУТАЦИЯ: замена in на not in
    #     return title not in self.available_books

    # MUT-LIB-05
    def get_total_books(self) -> int:
        return len(self.available_books) + len(self.borrowed_books)

    # def get_total_books(self) -> int:
    #     # МУТАЦИЯ: замена знака + на -
    #     return len(self.available_books) - len(self.borrowed_books)