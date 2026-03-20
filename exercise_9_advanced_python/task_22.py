# Task 22: Write a function that accepts both *args and **kwargs and prints them.

def show_args_kwargs(*args, **kwargs):
    print("Positional arguments (*args):", args)
    print("Keyword arguments (**kwargs):", kwargs)


show_args_kwargs(1, True, "Dummy text", name="John")
