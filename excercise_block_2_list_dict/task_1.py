# Task 1: Generate 10 random numbers and calculate the sum of them.
import random

numbers = []

for i in range(10):
    numbers.append(random.randint(1, 100))

print(numbers)

sum = 0
for number in numbers:
    sum += number

print("sum: ", sum)
