import importlib
import sys
import questionary

TASKS = [
    (
        1,
        "Shopping list: show, add, or delete items stored in shopping_list.txt.",
        "task_1",
    ),
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
