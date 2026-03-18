from pathlib import Path
from collections import Counter
import string
from questionary import text

TASK_TEXT_PATH = Path(__file__).parent / "task_10.txt"

search_word = text("Enter a word to search:").ask().lower()

with open(TASK_TEXT_PATH, encoding="utf-8") as file:
    lines = file.readlines()

    translator = str.maketrans("", "", string.punctuation)
    all_words = []
    for line in lines:
        words = line.translate(translator).lower().split()
        all_words.extend(words)

    word_counter = Counter(all_words)
    found_words_count = word_counter[search_word]
    if found_words_count == 0:
        print("Not found any place with this word.")
    else:
        print(
            f"\nThe word '{search_word}' appears {found_words_count} times.\n"
        )

        for line in (lines):
            if search_word in line.translate(translator).lower().split():
                print(line)
