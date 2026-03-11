# Task 5: Create two lists of names and print all the names
# but display only those names that are from the first list and not in the second list.

names_1 = ["John", "Alice", "Frank", "Albert", "Sophia"]
names_2 = ["Sarah", "Adam", "Albert", "John", "Martha"]

names_in_first_list_but_not_in_second = set(names_1) - (set(names_2))

print(names_in_first_list_but_not_in_second)
