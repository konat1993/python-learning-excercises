# Task 12: Let the user add items to a shopping list
# and save the list to a text file.

from pathlib import Path
import questionary

product_to_add = questionary.text(
    "Add products to shopping list"
).ask()

with open(Path(__file__).parent / "task_12.txt", "a+") as file:
    file.write(f"- {product_to_add}\n")

    file.seek(0)
    print(file.read())
