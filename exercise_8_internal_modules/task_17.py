# Task 17: Application to create, delete, and update tasks stored in JSON (title, description, status).

import json
import sys
from pathlib import Path
from typing import TypedDict

import questionary

TODOS_JSON_PATH = Path(__file__).parent / "task_17.json"


class Todo(TypedDict):
    id: int
    name: str
    description: str
    status: str


TodoList = list[Todo]
STATUSES = ["in progress", "done"]


def load_todos() -> TodoList:
    if not TODOS_JSON_PATH.exists():
        return []
    raw = TODOS_JSON_PATH.read_text().strip()
    if not raw:
        return []
    todos = json.loads(raw)
    return todos


def save_todos(todos: TodoList):
    TODOS_JSON_PATH.write_text(json.dumps(todos, indent=4))


def choose_todo(todos: TodoList, prompt: str) -> Todo | None:
    if not todos:
        print("No todos available.")
        return None
    choices = [
        {
            "name": f"{todo['id']}: {todo['name']} [{todo['status']}]",
            "value": todo["id"],
        }
        for todo in todos
    ]
    selected_id = questionary.select(prompt, choices=choices).ask()
    if selected_id is None:
        return None
    return next((todo for todo in todos if todo["id"] == selected_id), None)


def add_todo():
    todos = load_todos()
    name = questionary.text("Enter todo name: ").ask()
    if not name or not name.strip():
        print("Todo name cannot be empty.")
        return
    description = questionary.text("Enter todo description: ").ask()
    if not description or not description.strip():
        print("Todo description cannot be empty.")
        return

    next_id = max((todo["id"] for todo in todos), default=0) + 1
    todos.append(
        {
            "id": next_id,
            "name": name.strip(),
            "description": description.strip(),
            "status": "in progress",
        }
    )
    save_todos(todos)
    print("Todo added successfully.")


def delete_todo():
    todos = load_todos()
    todo = choose_todo(todos, "Select todo to delete:")
    if todo is None:
        return
    todos.remove(todo)
    save_todos(todos)
    print(f"Todo with id {todo['id']} deleted successfully.")


def update_todo():
    todos = load_todos()
    todo = choose_todo(todos, "Select todo to update:")
    if todo is None:
        return

    new_name = questionary.text(
        "Enter new todo name:", default=todo["name"]).ask()
    if not new_name or not new_name.strip():
        print("Todo name cannot be empty.")
        return

    new_description = questionary.text(
        "Enter new todo description:",
        default=todo["description"],
    ).ask()
    if not new_description or not new_description.strip():
        print("Todo description cannot be empty.")
        return

    new_status = questionary.select(
        "Select new status:",
        choices=STATUSES,
        default=todo["status"],
    ).ask()
    if new_status is None:
        print("Status update cancelled.")
        return

    todo["name"] = new_name.strip()
    todo["description"] = new_description.strip()
    todo["status"] = new_status
    save_todos(todos)
    print(f"Todo with id {todo['id']} updated successfully.")


MAIN_MENU = [
    {"name": "Add todo", "value": "ADD"},
    {"name": "Delete todo", "value": "DELETE"},
    {"name": "Update todo", "value": "UPDATE"},
    {"name": "Exit", "value": "EXIT"},
]


ACTIONS = {
    "ADD": add_todo,
    "DELETE": delete_todo,
    "UPDATE": update_todo,
}


def main():
    while True:
        answer = questionary.select(
            "What would you like to do?", choices=MAIN_MENU
        ).ask()
        if answer is None or answer == "EXIT":
            break
        if answer in ACTIONS:
            ACTIONS[answer]()


if __name__ == "__main__":
    main()
