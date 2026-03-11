import importlib
import sys
import questionary

TASKS = [
    (1, "Generate 10 random numbers and calculate the sum of them.", "task_1"),
    (2, "Print all words that have more than 5 letters.", "task_2"),
    (3, "Find the highest and lowest number in the list.", "task_3"),
    (4, "Create two sets of names and print common names.", "task_4"),
    (
        5,
        "Print names that are in the first list but not in the second list.",
        "task_5",
    ),
    (6, "Create a dictionary of countries and their capitals and print them.", "task_6"),
    (7, "Sort the countries by country name and print them.", "task_7"),
    (8, "Count the number of occurrences of each word in the sentence.", "task_8"),
]

for i, (num, desc, mod_name) in enumerate(TASKS):
    prefix = "\n" if i > 0 else ""
    print(f"{prefix}Task {num}: {desc}")
    run = questionary.select(
        "Do you want to run this task?", choices=["Yes", "No"]
    ).ask()

    if run == "Yes":
        importlib.import_module(mod_name)
    else:
        choice = questionary.select(
            "Proceed to next task or exit?", choices=["Next", "Exit"]
        ).ask()
        if choice == "Exit":
            print("Goodbye!\n")
            sys.exit(0)


print("\nAll tasks done.")
