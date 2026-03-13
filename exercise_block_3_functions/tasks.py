import importlib
import sys
import questionary

TASKS = [
    (1, "Add two numbers and return their sum.", "task_1"),
    (2, "Check if a number is even (True) or odd (False).", "task_2"),
    (3, "Compute the factorial of an integer n.", "task_3"),
    (4, "Reverse the given string without using reversed().", "task_4"),
    (5, "Check if a string is a palindrome.", "task_5"),
    (6, "Convert Celsius temperature to Fahrenheit.", "task_6"),
    (7, "Return a Fibonacci sequence of length n.", "task_7"),
    (
        8,
        "Return a sentence with name and age using an f-string.",
        "task_8",
    ),
    (9, "Return every second character from a given text.", "task_9"),
    (
        10,
        "Return a message depending on whether a number is positive, negative, or zero.",
        "task_10",
    ),
    (
        11,
        "Return the name of the day of the week for a given number using match/case.",
        "task_11",
    ),
    (
        12,
        "Return the union, difference, and intersection of two sets.",
        "task_12",
    ),
    (
        13,
        "Return the combined list of keys from two dictionaries.",
        "task_13",
    ),
    (
        14,
        "Return the largest, smallest, and the sum of numbers in a list.",
        "task_14",
    ),
    (
        15,
        "Return the list of names in reverse order using a loop.",
        "task_15",
    ),
    (
        16,
        "Return the area of a rectangle given its length and width.",
        "task_16",
    ),
    (
        17,
        "Return numbers from a list that appear more than once.",
        "task_17",
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

