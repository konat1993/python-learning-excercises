# Task 8: Create a dictionary with numbers 1 to 10 as keys
# and their squares as values, but only for even numbers,
# using dictionary comprehension.

numbers = [num for num in range(1, 11)]

even_squares = {num: num**2 if num % 2 == 0 else num for num in numbers}
print(even_squares)
