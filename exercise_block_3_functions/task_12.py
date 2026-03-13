# Task 12: Write a function that takes two sets and returns their union, difference, and intersection.

def get_set_sum_diff_intersection(setA: set, setB: set):
    return {
        "sum": setA.union(setB),
        "diff": setA.difference(setB),
        "intersection": setA.intersection(setB)
    }


print(get_set_sum_diff_intersection(
    {"1", "2", "4"},
    {"3", "2", "4"}
))
