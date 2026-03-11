# Task 6: Display the sum of all even numbers in the range 1–100.
evenSum = 0

for i in range(0, 101):
    if i % 2 == 0:
        evenSum += i

print(evenSum)
