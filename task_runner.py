import importlib
import sys
from pathlib import Path

import questionary


def run_block(block_name):
    block_dir = Path(__file__).resolve().parent / block_name
    if not block_dir.is_dir():
        print(f"Block not found: {block_dir}\n")
        sys.exit(1)
    sys.path.insert(0, str(block_dir))
    mod = importlib.import_module("tasks")
    run_tasks(mod.TASKS)
    print("\nAll tasks done.")


def run_tasks(tasks):
    for i, (num, desc, mod_name) in enumerate(tasks):
        prefix = "\n" if i > 0 else ""
        print(f"{prefix}Task {num}: {desc}")
        run = questionary.select(
            "Do you want to run this task?", choices=["Yes", "No"]
        ).ask()

        if run == "Yes":
            module = importlib.import_module(mod_name)
            module_main = getattr(module, "main", None)
            if callable(module_main):
                try:
                    module_main()
                except Exception as e:
                    print(f"Task failed with error: {e}")
                    print("Continuing to the next task.")
        else:
            choice = questionary.select(
                "Proceed to next task or exit?", choices=["Next", "Exit"]
            ).ask()
            if choice == "Exit":
                print("Goodbye!\n")
                sys.exit(0)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python task_runner.py <block_folder>\n")
        sys.exit(1)
    run_block(sys.argv[1])
