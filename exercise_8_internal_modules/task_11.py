# Task 11: Read a text file, count sentences, words, and characters;
# save results to a CSV file.

import csv
from pathlib import Path
import string

TASK_TEXT_PATH = Path(__file__).parent / "task_11.txt"
TASK_CSV_PATH = Path(__file__).parent / "task_11.csv"


def save_to_csv(sentence_count, words_count, characters_count):
    try:
        with open(TASK_CSV_PATH, "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(
                csv_file,
                fieldnames=["sentence_count",
                            "words_count", "characters_count"]
            )
            writer.writeheader()
            writer.writerow({
                "sentence_count": sentence_count,
                "words_count": words_count,
                "characters_count": characters_count
            })
        print(f"See the data in the file: {TASK_CSV_PATH.split('/')[-1]}")

    except Exception as e:
        print(e)


def count_sentences(text: str) -> int:
    sentences = [s for s in text.split(".") if s.strip()]
    return len(sentences)


def count_words(text: str) -> int:
    translator = str.maketrans("", "", string.punctuation)
    return len(text.translate(translator).split())


def count_characters(text: str) -> int:
    return len(text)


def main():
    with open(TASK_TEXT_PATH, encoding="utf-8") as txt_file:
        text = txt_file.read()

    sentence_count = count_sentences(text)
    words_count = count_words(text)
    characters_count = count_characters(text)

    save_to_csv(sentence_count, words_count, characters_count)


if __name__ == "__main__":
    main()
