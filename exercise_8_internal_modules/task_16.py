# Task 16: Generate random passwords of given length
# (letters, digits, special chars); save to text file.

from pathlib import Path
import random
import string

PASSWORD_TEXT_PATH = Path(__file__).parent / "task_16.txt"


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


def save_to_file(password):
    try:
        with open(PASSWORD_TEXT_PATH, 'w') as file:
            file.write(password + '\n')
        print(f"Passwords saved to {PASSWORD_TEXT_PATH.split('/')[-1]}")

    except Exception as e:
        print(e)


def main():
    length = int(input("Enter the length of the password: "))
    password = generate_password(length)
    save_to_file(password)


if __name__ == "__main__":
    main()
