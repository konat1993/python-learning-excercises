# Task 12: Write a generator that yields numbers from 1 to 10.

def number_generator():
    for i in range(1, 11):
        yield i


for number in number_generator():
    print(number)
