# Task 1: Shopping list — interactive CLI to view, add, and remove items
# from a text-file shopping list (shopping_list.txt).

import sys
from pathlib import Path

import questionary

CHOICES = {
    "Show shopping list": "SHOW",
    "Add item to the list": "ADD",
    "Delete item from the list": "DELETE",
    "Exit program": "EXIT",
}

SHOPPING_LIST_PATH = Path(__file__).parent / "shopping_list.txt"


def display_questions():
    choice = questionary.select(
        "What would you like to do:",
        choices=CHOICES,
    ).ask()
    return choice


def read_list():
    try:
        with open(SHOPPING_LIST_PATH, "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        return []
    except OSError as e:
        print(f"Could not read the shopping list: {e}")
        raise


def add_item(item_to_add, content):
    if (item_to_add.lower() + "\n") in [item.lower() for item in content]:
        return False
    try:
        with open(SHOPPING_LIST_PATH, "a", encoding="utf-8") as f:
            f.write(item_to_add + "\n")
            f.flush()
        return True
    except OSError as e:
        print(f"Could not save the item: {e}")
        return False


def delete_item(delete_choice, content):
    new_lines = [item for item in content if item.strip() !=
                 delete_choice.strip()]
    try:
        with open(SHOPPING_LIST_PATH, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
            f.flush()
    except OSError as e:
        print(f"Could not remove item from the shopping list: {e}")
        raise


main_choice = display_questions()
if CHOICES[main_choice] == "EXIT":
    sys.exit()

questionary_count = 0
while True:
    if questionary_count > 0:
        main_choice = display_questions()
        if CHOICES[main_choice] == "EXIT":
            sys.exit()
    questionary_count += 1
    content = read_list()

    if CHOICES[main_choice] == "SHOW":
        if not content:
            print("The shopping list is empty. You can add your first item.")
        else:
            print("".join(content))

    if CHOICES[main_choice] == "ADD":
        item_to_add = input("Write an item: ")
        if not item_to_add or not item_to_add.strip():
            print("Item cannot be empty!")
        elif add_item(item_to_add, content):
            print("Item added.")
        else:
            print("This item already exists in the shopping list!")

    if CHOICES[main_choice] == "DELETE":
        if not content:
            print("The shopping list is empty.")
        else:
            delete_choice = questionary.select(
                "Which item would you like to remove?",
                choices=[item.strip("\n") for item in content] + ["Go Back"],
            ).ask()
            if delete_choice != "Go Back":
                delete_item(delete_choice, content)
                print("Item removed.")
