# Task 9: Get three integers from the user and sort them from smallest to largest.
# 1
# numbers = input("Enter a list of numbers: ")
# numbers = numbers.split(",")

# numbers.sort(key=float)  # or sorted(numbers, key=float)
# print(*numbers)

# 2
numbers = [
    int(input("Enter the first number: ")),
    int(input("Enter the second number: ")),
    int(input("Enter the third number: ")),
]

print(*sorted(numbers))


# 3
# a = 5
# b = 15
# c = 10

# if a > b:
#     a, b = b, a
# if a > c:
#     a, c = c, a
# if b > c:
#     b, c = c, b

# print(a, b, c)


# 4
# numbers = [5, 15, 10]

# n = len(numbers)

# for i in range(n):
#     for j in range(n - 1):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# print(numbers)
