import importlib
import sys
import questionary

TASKS = [
    (1, "Check if the user's number is even or odd.", "task_1"),
    (
        2,
        "Check if the user's number is greater than 0, less than 0, or equal to 0.",
        "task_2",
    ),
    (
        3,
        "Ask for an exam score (0–100) and display the grade: 90–100 → 5, 80–89 → 4, 70–79 → 3, 60–69 → 2, below 60 → 1.",
        "task_3",
    ),
    (4, "Display numbers from 0 to 100.", "task_4"),
    (5, "Display all prime numbers from 1 to 100.", "task_5"),
    (6, "Display the sum of all even numbers in the range 1–100.", "task_6"),
    (7, "Compute the area of a rectangle (user provides side lengths).", "task_7"),
    (8, "Check if the given sentence is valid (ends with a period).", "task_8"),
    (
        9,
        "Get three integers from the user and sort them from smallest to largest.",
        "task_9",
    ),
    (
        10,
        "Guessing game — pick a random number 1–100, ask the user to guess; after each try show if the guess is higher or lower; end when correct.",
        "task_10",
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
