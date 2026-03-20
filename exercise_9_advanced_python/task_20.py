# Task 20: Write a function that accepts any
# number of numeric arguments and returns their sum.

def sum_numbers(*args):
    return sum(args)


print(sum_numbers(1, 2, 3, 4))
