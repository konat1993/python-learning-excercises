# Task 29: Write a function that returns another function as its result,
# then call the returned function.

def greet(name: str):
    return f"Hello, {name}!"


def greet_wrapper():
    return greet


greet_function = greet_wrapper()
print(greet_function("John"))
