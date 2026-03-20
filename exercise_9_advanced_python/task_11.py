# Task 11: Use the walrus operator to assign a user-entered number
# and check whether it is positive in the same expression.

number = int(input("Write an integer: "))

if (is_positive := number > 0):
    print("The number is positive", is_positive)
else:
    print("The number is negative", is_positive)
