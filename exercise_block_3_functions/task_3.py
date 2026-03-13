# Task 3: Write a function factorial(n) that takes an integer n and returns its factorial (n!).

import math


def factorial(n: int) -> int:
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non‑negative integer")
    return math.factorial(n)


print(factorial(4))
