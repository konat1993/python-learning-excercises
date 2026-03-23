from books import Book, FictionBook, NonFictionBook
from users import User


class Initializer:
    @staticmethod
    def init_users() -> list[User]:
        return [
            User("John"),
            User("Adam"),
            User("Sarah")
        ]

    @staticmethod
    def init_books() -> list[Book]:
        book1 = FictionBook(
            "Interstellar",
            "John Doe",
            200,
            True,
            "Science fiction",
            "A journey through space and time.",
        )
        book2 = NonFictionBook(
            "Python in Practice",
            "Jane Smith",
            148,
            True,
            "Programming",
            "Beginner",
        )

        return [book1, book2]
