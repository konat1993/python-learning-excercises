# Task 27: Use all() and any() to test whether
# all or some elements in a list satisfy a given condition.

def get_if_only_even(numbers):
    return all(num % 2 == 0 for num in numbers)


def get_if_only_odd(numbers):
    return all(num % 2 != 0 for num in numbers)


def get_if_some_even(numbers):
    return any(num % 2 == 0 for num in numbers)


def get_if_some_odd(numbers):
    return any(num % 2 != 0 for num in numbers)


even_and_odd_numbers = [2, 5]
print(
    f"Are only even {even_and_odd_numbers}: {get_if_only_even(even_and_odd_numbers)}")
print(
    f"Are only odd {even_and_odd_numbers}: {get_if_only_odd(even_and_odd_numbers)}")

print(
    f"Are some even {even_and_odd_numbers}: {get_if_some_even(even_and_odd_numbers)}")
print(
    f"Are some odd {even_and_odd_numbers}: {get_if_some_odd(even_and_odd_numbers)}")


only_even_numbers = [2, 4]
print(
    f"Are only even {only_even_numbers}: {get_if_only_even(only_even_numbers)}")
print(
    f"Are only odd {only_even_numbers}: {get_if_only_odd(only_even_numbers)}")

print(
    f"Are some even {only_even_numbers}: {get_if_some_even(only_even_numbers)}")
print(
    f"Are some odd {only_even_numbers}: {get_if_some_odd(only_even_numbers)}")
