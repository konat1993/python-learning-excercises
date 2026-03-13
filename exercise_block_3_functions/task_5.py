# Task 5: Write a function is_palindrome(s) that returns True if the string is a palindrome and False otherwise.


def is_palindrome(s: str):
    sanitized = s.strip().casefold().translate(str.maketrans("", "", ",.' "))
    return sanitized == sanitized[::-1]


print(is_palindrome("I am not palindrome"))

print(is_palindrome("Madam, I'm Adam."))
