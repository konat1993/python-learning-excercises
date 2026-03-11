#  Task 2: Print all words that have more than 5 letters.

words = [
    "one",
    "hundred",
    "six",
    "seven",
    "table",
    "apple",
    "egg",
    "house",
    "door",
    "window",
]

more_than_5_letter_words = []

for word in words:
    if len(word) >= 5:
        more_than_5_letter_words.append(word)

print(more_than_5_letter_words)
