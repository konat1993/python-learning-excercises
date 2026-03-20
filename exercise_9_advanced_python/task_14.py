# Task 14: Assign a function to a variable
# and call the function through that variable.

names = ["John", "Alice", "Frank", "Albert", "Sophia"]


def get_first_letters(names_list: list):
    return [name[0] for name in names_list]


first_letters = get_first_letters
print(first_letters(names))
