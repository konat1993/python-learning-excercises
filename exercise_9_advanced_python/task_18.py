# Task 18: Write a decorator that counts how many times
# the decorated function has been called.


def count_calls(fn):
    i = 0

    def wrapper(*args, **kwargs):
        fn(*args, **kwargs)
        nonlocal i
        i += 1
        print(f"Function called {i} {'times' if i > 1 else 'time.'}")

    return wrapper


@count_calls
def dummy_function():
    print("I am dummy function")


dummy_function()
dummy_function()
dummy_function()
