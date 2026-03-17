# Task 14: Write a function that takes a list of numbers and returns the largest, the smallest, and the sum of the numbers.

def get_sum_lowest_highest(number_list: list):
    return {
        "lowest": min(number_list),
        "highest": max(number_list),
        "sum": sum(number_list)
    }


print(get_sum_lowest_highest([3, 5, 1, 8]))
