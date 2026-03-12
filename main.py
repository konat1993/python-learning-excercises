"""
Launcher: choose which task block to run.
You can also run each block separately from its folder:
  cd exercise_block_1_basics && python tasks.py
  cd exercise_block_2_list_dict && python tasks.py
"""

import importlib
import sys
from pathlib import Path

import questionary

BLOCKS = [
    ("Block 1: Basics (tasks 1–10)", "exercise_block_1_basics"),
    ("Block 2: List & Dict (tasks 1–8)", "exercise_block_2_list_dict"),
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

# Run the block's main.py — add the block folder to the start of sys.path
# so that task_1, task_2, etc. are imported from that folder
sys.path.insert(0, str(block_dir))
with open(main_path) as f:
    code = compile(f.read(), main_path, "exec")
    exec_globals = {
        "__name__": "__tasks__",
        "__file__": str(main_path),
        "importlib": importlib,
        "sys": sys,
        "questionary": questionary,
    }
    exec(code, exec_globals)
