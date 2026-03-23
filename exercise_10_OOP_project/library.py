from books import Book, BookNotAvailableError, BookNotFoundError
from initializer import Initializer


class Library:
    def __init__(self) -> None:
        self.books: list[Book] = Initializer.init_books()

    def borrow_book(self, title: str) -> Book:
        normalized_title = title.lower().strip()
        for book in self.books:
            if book.title.lower() != normalized_title:
                continue
            if not book.available:
                raise BookNotAvailableError("Book is not available")
            book.available = False
            return book
        raise BookNotFoundError("Book not found")

    def return_book(self, title: str) -> Book:
        normalized_title = title.lower().strip()
        for book in self.books:
            if book.title.lower() == normalized_title:
                book.available = True
                return book
        raise BookNotFoundError("Book not found")

    def display_books(self) -> None:
        if not self.books:
            print("Library is empty.")
            return
        for book in self.books:
            book.display_book_info()
