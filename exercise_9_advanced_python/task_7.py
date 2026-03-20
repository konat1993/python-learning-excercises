# Task 7: Create a dictionary with keys 1 to 5
# and values equal to their squares, using dictionary comprehension.

numbers = [1, 2, 3, 4, 5]

k_v_to_square = {num: num**2 for num in numbers}
print(k_v_to_square)
