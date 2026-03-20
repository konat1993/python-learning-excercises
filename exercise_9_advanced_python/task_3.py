# Task 3: Create a list with "even" or "odd" for each number from 1 to 10 using list comprehension.

even_odd_list = ["Even" if num % 2 == 0 else "Odd" for num in range(1, 11)]
print(even_odd_list)
