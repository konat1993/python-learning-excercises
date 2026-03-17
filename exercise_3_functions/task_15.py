# Task 15: Write a function that takes a list of names and prints them in reverse order using a loop.


# def get_reversed_names(names_list):
#     return names_list[::-1]
#     return list(reversed(names_list))

def get_reversed_names(names_list: list):
    reversed_list = []
    for i in range(0, len(names_list)):
        reversed_list.append(names_list[len(names_list) - (i + 1)])

    return reversed_list


print(get_reversed_names([
    "John",
    "Anna",
    "Phillip",
    "Martha",
    "Claudia"
]))
