# Task 17: Write a function that takes a list of numbers and returns those that appear more than once in the list.

from collections import Counter


# def get_duplicates(numbers_list: list):
#     duplicates = []
#     tempSet = {}

#     for i in range(0, len(numbers_list)):
#         if tempSet.get(numbers_list[i]) != None:
#             print(numbers_list[i])
#             duplicates.append(numbers_list[i])
#         else:
#             tempSet[numbers_list[i]] = True

#     return duplicates


def get_duplicates(numbers):
    counts = Counter(numbers)

    # duplicates = []
    # for n, count in counts.items():
    #     if count > 1:
    #         duplicates.append(n)
    # return duplicates
    return [n for n, count in counts.items() if count > 1]


print(get_duplicates([1, 2, 5, 7, 3, 2, 5, 10]))
