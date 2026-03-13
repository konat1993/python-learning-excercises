# Task 13: Write a function that takes two dictionaries and returns a list of keys from both dictionaries.

def get_merged_keys(d1: dict, d2: dict) -> list:
    d1_keys = d1.keys()
    d2_keys = d2.keys()

    return list(d1_keys | d2_keys)


print(get_merged_keys({"1": "one", "2": "two"}, {"3": "three"}))
