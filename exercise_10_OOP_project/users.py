from books import Book, BookNotFoundError


class User:
    def __init__(self, name: str) -> None:
        self.name = name
        self.books: list[Book] = []

    def display_books(self) -> None:
        if not self.books:
            print("You have not borrowed any books yet.")
            return
        for book in self.books:
            book.display_book_info()

    def borrow_book(self, book: Book) -> None:
        self.books.append(book)

    def return_book(self, title: str) -> Book:
        normalized_title = title.lower().strip()
        for book in self.books:
            if book.title.lower() == normalized_title:
                self.books.remove(book)
                return book

        raise BookNotFoundError("Book not found in your books")


class UserNotFoundError(Exception):
    pass
