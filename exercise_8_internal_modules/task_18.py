# Task 18: Quiz app with questions from categories,
# four choices, one correct; JSON storage; category choice and final score.

import json
import random
from pathlib import Path

import questionary

QUIZ_JSON_PATH = Path(__file__).parent / "task_18.json"


def load_quiz_data():
    return json.loads(QUIZ_JSON_PATH.read_text() or "[]")


def get_questions_for_category(quiz_data, category_name):
    for category in quiz_data:
        if category["category"] == category_name:
            return category["questions"]
    return []


def main():
    print("Let's start the quiz!")
    quiz_data = load_quiz_data()

    if not quiz_data:
        print("No quiz data found.")
        return

    categories = [item["category"] for item in quiz_data]
    score = 0
    answered_questions = 0

    while True:
        round_score = 0
        round_questions = 0
        category = questionary.select(
            "Select category:", choices=categories).ask()
        if category is None:
            break

        questions = get_questions_for_category(quiz_data, category)
        if not questions:
            print("No questions in this category.")
            continue

        for index, question in enumerate(random.sample(questions, k=len(questions)), start=1):
            shuffled_answers = random.sample(
                [{"name": answer, "value": answer}
                    for answer in question["answers"]],
                k=len(question["answers"]),
            )

            answer = questionary.select(
                f"Question {index}: {question['question']}",
                choices=shuffled_answers,
            ).ask()

            if answer is None:
                print("Quiz interrupted.")
                print(f"Final score: {score}/{answered_questions}")
                return

            answered_questions += 1
            round_questions += 1
            if answer == question["correct_answer"]:
                score += 1
                round_score += 1
                print("Correct!")
            else:
                print(
                    f"Incorrect! Correct answer: {question['correct_answer']}")

        print(f"Current score: {round_score}/{round_questions}")
        should_continue = questionary.select(
            "Do you want to start again?", choices=["Yes", "No"]
        ).ask()
        if should_continue is None or should_continue == "No":
            break
        if should_continue == "Yes":
            score = 0
            answered_questions = 0
            continue

    print(f"Final score: {score}/{answered_questions}")


if __name__ == "__main__":
    main()
