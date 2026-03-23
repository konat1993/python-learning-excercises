# Task 1: Build a library simulator.
# The three most important features are:
# 1. Display books borrowed by the current user.
# 2. Display all books in the library with availability status.
# 3. Borrow and return books.
#
# Additional requirements:
# - At startup, ask for the user name.
# - Allow changing the active user during one app session.
# - Keep book availability shared across users (if John borrows A/B,
#   these books are unavailable to Adam and everyone else).
# - Pre-populate both books and users at startup.
# - Define books and users as classes.
# - Support two book types: fiction and nonfiction.
# - Define custom exceptions:
#   user not found, book not found, and borrowing unavailable book.

import sys

from questionary import select, text

from books import BookNotAvailableError, BookNotFoundError
from initializer import Initializer
from library import Library
from users import User, UserNotFoundError

MENU_CHOICES = [
    {"name": "List all library books", "value": "LIB_BOOKS"},
    {"name": "Show my borrowed books", "value": "USER_BOOKS"},
    {"name": "Borrow a book", "value": "BORROW"},
    {"name": "Return a book", "value": "RETURN"},
    {"name": "Switch user", "value": "SWITCH_USER"},
    {"name": "Exit", "value": "EXIT"},
]


def display_library_books(library: Library) -> None:
    library.display_books()


def display_borrowed_books(user: User) -> None:
    user.display_books()


def borrow_book(user: User, library: Library) -> None:
    title = text("Enter the title of the book you want to borrow:").ask()
    if title is None:
        return

    try:
        book = library.borrow_book(title)
        user.borrow_book(book)
        print("Book borrowed successfully.")
    except BookNotFoundError:
        print("Book not found.")
    except BookNotAvailableError:
        print("Book is already borrowed.")


def return_book(user: User, library: Library) -> None:
    title = text("Enter the title of the book you want to return:").ask()
    if title is None:
        return

    try:
        user.return_book(title)
        library.return_book(title)
        print("Book returned successfully.")
    except BookNotFoundError:
        print("Book not found in your borrowed books.")


def login_user(users: list[User], user_choice: str) -> User:
    normalized_name = user_choice.lower().strip()
    for user in users:
        if user.name.lower() == normalized_name:
            return user
    raise UserNotFoundError("User not found")


def prompt_for_user(users: list[User]) -> User:
    while True:
        try:
            user_choice = text("What is your name?").ask()
            if user_choice is None:
                sys.exit()
            user = login_user(users, user_choice)
            print(f"Welcome, {user.name}!")
            return user
        except UserNotFoundError:
            print("User not found. Try one of the preloaded users.")


def main() -> None:
    library = Library()
    users = Initializer.init_users()
    user = prompt_for_user(users)

    while True:
        selection = select("Choose option:", choices=MENU_CHOICES).ask()
        if selection is None or selection == "EXIT":
            sys.exit()
        if selection == "LIB_BOOKS":
            display_library_books(library)
        elif selection == "USER_BOOKS":
            display_borrowed_books(user)
        elif selection == "BORROW":
            borrow_book(user, library)
        elif selection == "RETURN":
            return_book(user, library)
        elif selection == "SWITCH_USER":
            user = prompt_for_user(users)


if __name__ == "__main__":
    main()
