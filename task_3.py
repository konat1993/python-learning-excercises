# Task 3: Ask for an exam score (0–100) and display the grade: 90–100 → 5, 80–89 → 4, 70–79 → 3, 60–69 → 2, below 60 → 1.

while True:
    score = int(input("Enter a score: "))
    if 0 <= score <= 100:
        break
    print("The score must be between 0 and 100. Try again.")

if score >= 90:
    print(5)
elif score >= 80:
    print(4)
elif score >= 70:
    print(3)
elif score >= 60:
    print(2)
else:
    print(1)

# match score:
#     case score if score >= 90:
#         print(5)
#     case score if score >= 80:
#         print(4)
#     case score if score >= 70:
#         print(3)
#     case score if score >= 60:
#         print(2)
#     case _:
#         print(1)
