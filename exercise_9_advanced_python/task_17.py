# Task 17: Write a decorator that measures
# how long the decorated function takes to execute.


from time import time as tm


def measure_execution_time(fn):
    def wrapper(*args, **kwargs):
        start_time = tm()
        fn(*args, **kwargs)
        end_time = tm()
        print(f"Time taken: {end_time - start_time} seconds")
    return wrapper


@measure_execution_time
def add_sum_by_count(number: int):
    print(sum(range(number)))


add_sum_by_count(100)
