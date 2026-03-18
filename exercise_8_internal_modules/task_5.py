# Task 5: Ask the user to provide several names and save them to a text file.

from pathlib import Path
import questionary
import sys

TASK_5_TEXT_PATH = Path(__file__).parent / "task_5.txt"


def add_names_to_file():
    while True:
        choice = questionary.select(
            "Add names or exit",
            choices=[
                {"value": "ADD", "name": "Add names"},
                {"value": "EXIT", "name": "Exit"}
            ]
        ).ask()
        if choice is None or choice == "EXIT":
            break

        names_input = questionary.text(
            "Enter names separated by commas or line breaks: ").ask()
        if names_input is None:
            break

        names = [name.strip() for part in names_input.split('\n')
                 for name in part.split(',') if name.strip()]
        if names:
            with open(TASK_5_TEXT_PATH, "a") as file:
                for name in names:
                    file.write(name + "\n")
            print(
                f"Names added to the task_5.txt file: {', '.join(names)}")
        else:
            print("No valid names entered.")


add_names_to_file()
