# Task 10: Use the walrus operator to assign a number
# and check whether it is even in the same expression.

number = int(input("Write an integer: "))

if (remainder := number % 2) == 0:
    print(f"The number is EVEN. Remainder={remainder}")
else:
    print(f"The number is ODD Remainder={remainder}")
