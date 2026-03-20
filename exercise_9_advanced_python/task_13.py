# Task 13: Write a generator that yields the first 10 Fibonacci numbers.

def fibonacci_generator():
    a, b = 0, 1
    for _ in range(10):
        yield a
        a, b = b, a + b


for number in fibonacci_generator():
    print(number)
