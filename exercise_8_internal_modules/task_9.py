# Task 9: Ask user for two numbers and an operation (addition, subtraction, multiplication, division); handle division by zero and invalid input.

from questionary import select, text
from decimal import Decimal


def _validate_numbers(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Numbers must be valid.")
    return Decimal(str(a)), Decimal(str(b))


def add(a, b):
    x, y = _validate_numbers(a, b)
    return x + y


def subtract(a, b):
    x, y = _validate_numbers(a, b)
    return x - y


def multiply(a, b):
    x, y = _validate_numbers(a, b)
    return x * y


def divide(a, b):
    x, y = _validate_numbers(a, b)
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y


OPERATIONS = [
    {"value": add, "name": "Addition"},
    {"value": subtract, "name": "Subtraction"},
    {"value": multiply, "name": "Multiplication"},
    {"value": divide, "name": "Division"},
]


def get_operation():
    return select("Select an operation", choices=OPERATIONS).ask()


def get_numbers():
    while True:
        try:
            first = text("Enter the first number: ").ask()
            if first is None:
                return None
            second = text("Enter the second number: ").ask()
            if second is None:
                return None
            return [float(first), float(second)]

        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue
        except Exception as e:
            print(f"Error: {e}")
            return None


def format_result(value, decimals=2):
    result = round(float(value), decimals)
    return f"{result}".rstrip("0.")


def main():
    operation = get_operation()
    if operation is None:
        print("Operation cancelled.")
        return

    numbers = get_numbers()
    if numbers is None:
        print("Input cancelled.")
        return

    try:
        result = operation(numbers[0], numbers[1])
        print(format_result(result))
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
