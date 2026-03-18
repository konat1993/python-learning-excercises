# Task 3: Function that takes a number and raises ValueError if the number is negative.

def raise_value_error_if_negative(number: int) -> int:
    if number < 0:
        raise ValueError("Number must be positive.")
    return number


try:
    print(raise_value_error_if_negative(10))
    print(raise_value_error_if_negative(-10))
except Exception as e:
    print(e)
