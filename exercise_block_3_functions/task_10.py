# Task 10: Write a function that takes a number and returns a message depending on whether it is positive, negative, or zero.

def check_number(number: int):
    if number < 0:
        return "Negative number"
    if number > 0:
        return "Positive number"
    return "Zero"


print(check_number(0))
print(check_number(10))
print(check_number(-8))
