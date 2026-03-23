from abc import ABC, abstractmethod


class Book(ABC):
    def __init__(self, title: str, author: str, pages: int, available: bool) -> None:
        super().__init__()
        self.title = title
        self.author = author
        self.pages = pages
        self.available = available

    @abstractmethod
    def display_concrete_book_info(self) -> None:
        """Display subtype-specific book attributes."""

    def display_book_info(self) -> None:
        print("┌" + "─" * 49 + "┐")
        self._print_field("Title", self.title)
        self._print_field("Author", self.author)
        self._print_field("Pages", self.pages)
        self.display_concrete_book_info()
        self._print_field("Available", "Yes" if self.available else "No")
        print("└" + "─" * 49 + "┘")

    @staticmethod
    def _print_field(label: str, value):
        print(f"│ {label:<10} {str(value):<36} │")


class NonFictionBook(Book):
    def __init__(
        self,
        title: str,
        author: str,
        pages: int,
        available: bool,
        subject: str,
        level: str,
    ) -> None:
        super().__init__(title, author, pages, available)
        self.subject = subject
        self.level = level

    def display_concrete_book_info(self) -> None:
        self._print_field("Subject", self.subject)
        self._print_field("Level", self.level)


class FictionBook(Book):
    def __init__(
        self,
        title: str,
        author: str,
        pages: int,
        available: bool,
        genre: str,
        synopsis: str,
    ) -> None:
        super().__init__(title, author, pages, available)
        self.genre = genre
        self.synopsis = synopsis

    def display_concrete_book_info(self) -> None:
        self._print_field("Genre", self.genre)
        self._print_field("Synopsis", self.synopsis)


class BookNotFoundError(Exception):
    pass


class BookNotAvailableError(Exception):
    pass
