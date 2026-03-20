# Task 28: Combine two lists
# (e.g. first names and last names)
# into one list of tuples using zip.

names = ["John", "Adam", "Simon"]
last_names = ["Doe", "Smith", "Johnson"]

names_and_last_names = list(zip(names, last_names))

print(names_and_last_names)
