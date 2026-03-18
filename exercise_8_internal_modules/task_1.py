# Task 1: Divide a number by zero and handle ZeroDivisionError exception.

def divide_two_numbers(a: int, b: int) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero.")


try:
    print("10/2")
    print(divide_two_numbers(10, 2))
    print()
    print("10/0")
    print(divide_two_numbers(10, 0))
except Exception as e:
    print(e)
