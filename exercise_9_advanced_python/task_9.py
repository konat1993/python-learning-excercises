# Task 9: Use the walrus operator to assign a list
# and check its length in the same expression.

numbers = [1, 2, 3, 4, 5]

if (numbers := len(numbers)) > 3:
    print(numbers)
else:
    print("The list is too short")
