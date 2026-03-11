# Task 7: Compute the area of a rectangle (user provides side lengths).
a = float(input("Enter the length of the 1st side of the rectangle: "))
b = float(input("Enter the length of the 2nd side of the rectangle: "))

area = a * b
if area.is_integer():
    print(f"The area of the rectangle is {int(area)}")
else:
    print(f"The area of the rectangle is {area:.2f}")
