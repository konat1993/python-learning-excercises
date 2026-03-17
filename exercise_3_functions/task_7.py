# Task 7: Write a function fibonacci(n) that returns a Fibonacci sequence of length n.

def fibonacci(n):
    if n < 0:
        raise ValueError("n must be non‑negative")

    a = 0
    b = 1
    sequence = []

    for i in range(n):
        sequence.append(a)
        a, b = b, a + b

    return sequence


print(fibonacci(8))
