# Task 16: Write a simple decorator that prints a message before
# and after the wrapped function runs.

def printer(fn):
    def wrapper(*args, **kwargs):
        print("Start")
        fn(*args, **kwargs)
        print("End")
    return wrapper


@printer
def greet(name):
    print(f"Hello {name}!")


greet("Simon")
