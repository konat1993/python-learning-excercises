import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean
import questionary


TASK_DIRECTORY = Path(__file__).parent
GRADES_CSV_PATH = TASK_DIRECTORY / "task_20.csv"
AVERAGES_CSV_PATH = TASK_DIRECTORY / "task_20_averages.csv"
GRADES_FIELDNAMES = ["student", "subject", "grade"]
AVERAGES_FIELDNAMES = ["student", "average_grade"]
SUBJECTS = ["Math", "History", "Biology"]


def add_score_to_subject_for_student(student, subject, score):
    try:
        with open(GRADES_CSV_PATH, "r", newline="") as file:
            grades = list(csv.DictReader(file, skipinitialspace=True))
    except FileNotFoundError:
        grades = []

    grades.append({"student": student, "subject": subject, "grade": score})

    with open(GRADES_CSV_PATH, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=GRADES_FIELDNAMES)
        writer.writeheader()
        writer.writerows(sorted(grades, key=lambda x: x["student"]))


def load_student_data():
    try:
        with open(GRADES_CSV_PATH, "r", newline="") as file:
            return list(csv.DictReader(file, skipinitialspace=True))
    except FileNotFoundError:
        return []


def calculate_averages():
    student_data = load_student_data()

    grades_by_student = defaultdict(list)
    for row in student_data:
        grades_by_student[row["student"] or []].append(int(row["grade"]))

    print(grades_by_student)

    return {
        student: mean(student_grades)
        for student, student_grades in grades_by_student.items()
    }


def write_averages_to_csv(avg):
    with open(AVERAGES_CSV_PATH, "w", newline="") as file:
        avg_csv_file = csv.DictWriter(file, fieldnames=AVERAGES_FIELDNAMES)
        avg_csv_file.writeheader()
        avg_csv_file.writerows(avg)


def main():
    students_data = load_student_data()
    students = list(dict.fromkeys(item["student"] for item in students_data))

    while True:
        student = questionary.select(
            "Choose student to assign new score: ",
            choices=students + ["Exit"]
        ).ask()

        if student == "Exit" or student is None:
            break

        subject = questionary.select(
            "Select subject: ",
            choices=SUBJECTS + [{"name": "Add new subject", "value": "ADD"}]
        ).ask()

        if subject is None:
            continue

        if subject == "ADD":
            subject = questionary.text(
                "Subject: "
            ).ask()

        while True:
            answer = questionary.text(f"Set the score for {student}").ask()

            if answer is None:
                break

            try:
                score = int(answer)
            except ValueError:
                print("Please enter a number!")
                continue

            if not (1 <= score <= 6):
                print("Score must be between 1 and 6!")
                continue

            add_score_to_subject_for_student(student, subject, score)
            avg_data = calculate_averages()
            avg_list = list(
                {
                    "student": item,
                    "average_grade": round(avg_data[item], 1)
                }
                for item in avg_data
            )
            write_averages_to_csv(avg_list)
            break


if __name__ == "__main__":
    main()

# def append_grade(student: str, subject: str, grade: int) -> None:
#     file_exists = GRADES_CSV_PATH.exists()

#     with open(GRADES_CSV_PATH, "a", newline="") as file:
#         writer = csv.DictWriter(file, fieldnames=GRADES_FIELDNAMES)

#         if not file_exists:
#             writer.writeheader()

#         writer.writerow(
#             {
#                 "student": student,
#                 "subject": subject,
#                 "grade": grade,
#             }
#         )


# def load_student_data() -> list[dict[str, str]]:
#     if not GRADES_CSV_PATH.exists():
#         return []

#     with open(GRADES_CSV_PATH, newline="") as file:
#         return list(csv.DictReader(file, skipinitialspace=True))


# def calculate_averages(grades_data: list[dict[str, str]]) -> dict[str, float]:
#     grades_by_student: dict[str, list[int]] = defaultdict(list)

#     for row in grades_data:
#         grades_by_student[row["student"]].append(int(row["grade"]))

#     return {
#         student: mean(student_grades)
#         for student, student_grades in grades_by_student.items()
#     }


# def write_averages(averages: dict[str, float]) -> None:
#     with open(AVERAGES_CSV_PATH, "w", newline="") as file:
#         writer = csv.DictWriter(file, fieldnames=AVERAGES_FIELDNAMES)
#         writer.writeheader()

#         for student in sorted(averages):
#             writer.writerow(
#                 {
#                     "student": student,
#                     "average_grade": f"{averages[student]:.2f}",
#                 }
#             )


# def collect_grades_from_teacher() -> None:
#     print("Enter grades. Leave student empty to finish.")

#     while True:
#         student = input("Student: ").strip()
#         if not student:
#             break

#         subject = input("Subject: ").strip()
#         grade = int(input("Grade: ").strip())

#         append_grade(student, subject, grade)


# collect_grades_from_teacher()
# all_grades = load_student_data()
# averages = calculate_averages(all_grades)
# write_averages(averages)

# print(f"Averages saved to: {AVERAGES_CSV_PATH}")
