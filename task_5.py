# Task 5: Display all prime numbers from 1 to 100.
# from math import sqrt


# for n in range(0, 101):
#     if n <= 1:
#         continue
#     print(f"sqrt of {n} is {int(sqrt(n))}")
#     for i in range(2, int(sqrt(n)) + 1):
#         print(i)
#         if n % i == 0:
#             print(f"{n} is not a prime number")
#             break
#     else:
#         print(f"{n} is a prime number")
count = 0
print("List of prime numbers: ")
for n in range(0, 101):
    if n <= 1:
        continue

    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            break
    else:
        count += 1
        print(f"{count}: {n}")

print(f"Total prime numbers: {count}")
