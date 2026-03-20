# Task 30: Write a function that returns a function
# which multiplies its argument by a given factor.


def multiply_by(x):
    def multiplier(n):
        return x * n
    return multiplier


times_2 = multiply_by(2)
print(times_2(4))
