# Task 21: Write a function that accepts any number of keyword arguments
# and returns them as a dict with keys sorted alphabetically.

def make_dict(**kwargs):
    sorted_keys = sorted(kwargs)
    return {key: kwargs[key] for key in sorted_keys}


print(make_dict(name="John", age=32))
