# Task 6: Create a set of unique characters from a given word using set comprehension.

sentence = "This is a custom sentence."

unique_chars = {char for char in sentence if char.isalpha()}

print(unique_chars)
