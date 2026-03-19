# Python Learning Project

This repository is a personal learning project for practicing Python through small exercises.
The goal is to learn by doing: each exercise contains tasks that can be run step by step.

## Project Purpose

- Practice Python fundamentals and problem-solving.
- Work through tasks interactively (task by task).
- Run single scripts directly when you want to focus on one specific exercise.

## Requirements

- Python `3.14` (see `.python-version`)
- Dependencies from `requirements.txt`

## Setup

Using `uv` (recommended):

```bash
uv sync
```

Using `pip`:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## How to Run Tasks

### 1) Run the interactive menu (`main.py`)

This is the best option if you want to go through blocks and tasks in order.

```bash
python main.py
```

or:

```bash
uv run main.py
```

You will see a menu where you can choose an exercise block, then decide for each task whether to run it.

### 2) Run one block directly

If you already know the block folder name, you can run it without opening the main menu:

```bash
python task_runner.py exercise_3_functions
```

or:

```bash
uv run task_runner.py exercise_3_functions
```

### 3) Run a single task file directly

Use this when you do **not** want to go through the whole process and only want one task.

```bash
python exercise_3_functions/task_7.py
```

or:

```bash
uv run exercise_3_functions/task_7.py
```

You can replace the path with any task file, for example:
- `exercise_1_basics/task_1.py`
- `exercise_2_list_dict/task_6.py`
- `exercise_8_internal_modules/task_20.py`

## Notes

- Most task files expose a `main()` function and can be run as standalone scripts.
- If a task imports local helpers from its exercise folder, run it from the project root (commands above already assume that).
