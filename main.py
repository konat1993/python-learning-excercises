import task_runner
import sys
from pathlib import Path

import questionary

BLOCKS = [
    ("Block 1: Basics (tasks 1-10)", "exercise_1_basics"),
    ("Block 2: List & Dict (tasks 1-8)", "exercise_2_list_dict"),
    ("Block 3: Functions (tasks 1-17)", "exercise_3_functions"),
    ("Exercise 4: Shopping list (task 1)", "exercise_4_shopping_list"),
    ("Exercise 5: Log analysis (task 1)", "exercise_5_log_analysis"),
    ("Exercise 6: Video Library management", "exercise_6_videos_library"),
    ("Exercise 7: Phone database management (task 1)", "exercise_7_phone_shop"),
    ("Exercise 8: Internal modules (tasks 1-20)", "exercise_8_internal_modules"),
    ("Exercise 9: Advanced Python (tasks 1-30)", "exercise_9_advanced_python"),
    ("Exercise 10: OOP project - library simulator (task 1)", "exercise_10_OOP_project"),
    ("Exercise 11: Pandas IMDB analysis (task 1)", "exercise_11_pandas"),
]

choice = questionary.select(
    "Which task block do you want to run?",
    choices=[c[0] for c in BLOCKS] + ["Exit"],
).ask()

if choice == "Exit":
    print("Goodbye!\n")
    sys.exit(0)

block_dir_name = next(c[1] for c in BLOCKS if c[0] == choice)
project_root = Path(__file__).resolve().parent
block_dir = project_root / block_dir_name
main_path = block_dir / "tasks.py"

if not main_path.exists():
    print(f"Not found: {main_path}\n")
    sys.exit(1)

task_runner.run_block(block_dir_name)
