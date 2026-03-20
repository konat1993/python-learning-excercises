# Task 19: Write a decorator that appends the exact time
# the function was called to the string returned by the function.

from datetime import datetime as dt


def add_timestamp(fn):
    def wrapper(*args, **kwargs):
        now = dt.now()
        text = fn(*args, **kwargs)
        print(f"{text} ({now:%H:%M:%S})")

    return wrapper


@add_timestamp
def get_dummy_text(text):
    return text


get_dummy_text("This is dummy text.")
