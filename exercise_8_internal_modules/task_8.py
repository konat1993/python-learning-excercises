# Task 8: Measure the execution time of a function that sums numbers from 1 to 1,000,000.

from time import time

start_time = time()

sum = 0
for i in range(1, 1000000):
    sum += i

end_time = time()
print("Sum: ", sum)
print(f"Time taken: {end_time - start_time} seconds")
