# Task 10: Guessing game — pick a random number 1–100, ask the user to guess; after each try show if the guess is higher or lower; end when correct.
import random

random_number = random.randint(1, 100)

while True:
    guessed_number = int(input("Enter a number between 1 and 100: "))

    if guessed_number < 1 or guessed_number > 100:
        print("The number you provided must be between 1 and 100. Try again.")
        continue

    if guessed_number == random_number:
        print(f"You've made it! The number was {random_number}")
        break

    prompt = "higher" if guessed_number > random_number else "lower"

    print(
        f"You've missed!\nYour guess number is {prompt} than the one drawn. Try again!"
    )
