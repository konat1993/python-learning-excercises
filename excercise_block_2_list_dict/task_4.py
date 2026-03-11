# Task 4: Create two sets of names and print common names.

names_1 = ["John", "Alice", "Frank", "Albert", "Sophia"]
names_2 = ["Sarah", "Adam", "Albert", "John", "Martha"]

common_names = set(names_1) & (set(names_2))

print(common_names)
