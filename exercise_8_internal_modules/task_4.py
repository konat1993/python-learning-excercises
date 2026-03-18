# Task 4: Read the contents of a text file and print them on the screen.

from pathlib import Path


TASK_4_TEXT_PATH = Path(__file__).parent / "task_4.txt"

with open(TASK_4_TEXT_PATH, "r") as file:
    print(file.read())
