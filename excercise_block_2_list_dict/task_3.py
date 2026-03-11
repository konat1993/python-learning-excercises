# Task 3: Find the highest and lowest number in the list.
import random

numbers = []

for i in range(10):
    numbers.append(random.randint(-100, 100))

print(numbers)

# lowest_number = min(numbers)
# highest_number = max(numbers)

# print(f"Lowest number: {lowest_number}")
# print(f"Highest number: {highest_number}")

lowest_number = numbers[0]
highest_number = numbers[0]

for number in numbers:
    if number < lowest_number:
        lowest_number = number
    if number > highest_number:
        highest_number = number

print(f"Lowest number: {lowest_number}")
print(f"Highest number: {highest_number}")
