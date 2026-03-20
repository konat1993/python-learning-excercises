# Task 15: Write a program that takes a function as an argument
# and calls it inside another function.

def greet(name: str):
    return f"Hello, {name}!"


def greet_wrapper(function: callable):
    def wrapper(name: str):
        return function(name)
    return wrapper


hello = greet_wrapper(greet)
print(hello("John"))
