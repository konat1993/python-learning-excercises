# Task 1: Phone database manager.
# Options: 1) Display phone info (name, color, memory, price)
# 2) Add phones  3) Edit phones  4) Delete phones
# 5) Load data on startup, save changes on exit.

import json
import sys
import questionary
from typing import TypedDict
from pathlib import Path

PHONES_JSON_PATH = Path(__file__).parent / "phones.json"

MAIN_MENU = [
    {"name": "Display phone list", "value": "DISPLAY"},
    {"name": "Add phone", "value": "ADD"},
    {"name": "Edit phone", "value": "EDIT"},
    {"name": "Delete phone", "value": "DELETE"},
    {"name": "Save and exit", "value": "SAVE"},
    {"name": "Exit", "value": "EXIT"},
]


class Specifications(TypedDict):
    color: str
    memory: int


class PhoneItem(TypedDict):
    name: str
    specifications: Specifications
    price: int


PhoneList = list[PhoneItem]


def _phone_choices(phones: PhoneList, exit_value: str = "-1"):
    return [
        {"name": f"{i}. {p['name']} ({p['specifications']['color']}, {p['specifications']['memory']} GB) – {p['price']}$", "value": i - 1}
        for i, p in enumerate(phones, start=1)
    ] + [{"name": "Exit", "value": exit_value}]


def _get_by_path(obj: dict, path: list[str]):
    for key in path:
        obj = obj[key]
    return obj


def _set_by_path(obj: dict, path: list[str], value):
    for key in path[:-1]:
        obj = obj[key]
    obj[path[-1]] = value


def display_phones(phones: PhoneList):
    if not phones:
        print("No phones in the list.\n")
        return
    for idx, phone in enumerate(phones, start=1):
        s = phone["specifications"]
        print(f"{idx}. {phone['name']} ({phone['price']}$)")
        print(f"   Color: {s['color']}, Memory: {s['memory']} GB\n")


def add_phone(phones: PhoneList):
    name = (questionary.text("Phone name:").ask() or "").strip()
    color = (questionary.text("Color:").ask() or "").strip()
    while True:
        memory_input = questionary.text("Memory (GB):").ask() or ""
        if memory_input.isdigit():
            memory = int(memory_input)
            break
        print("Memory must be a number.")
    while True:
        price_input = questionary.text("Price:").ask() or ""
        if price_input.isdigit():
            price = int(price_input)
            break
        print("Price must be a number.")
    phones.append({
        "name": name,
        "specifications": {"color": color, "memory": memory},
        "price": price,
    })


def edit_phone(phones: PhoneList):
    if not phones:
        print("No phones to edit.\n")
        return
    while True:
        idx = questionary.select(
            "Select phone to edit:", choices=_phone_choices(phones)).ask()
        if idx == "-1":
            break
        phone = phones[idx]
        while True:
            path = questionary.select(
                "Field to change:",
                choices=[
                    {"name": "name", "value": ["name"]},
                    {"name": "color", "value": ["specifications", "color"]},
                    {"name": "memory", "value": ["specifications", "memory"]},
                    {"name": "price", "value": ["price"]},
                    {"name": "Back", "value": None},
                ],
            ).ask()
            if path is None:
                break
            old = _get_by_path(phone, path)
            new_value = questionary.text(
                f"New value ({path[-1]}):", default=str(old)).ask()
            if new_value is None:
                continue
            if path == ["specifications", "memory"] or path == ["price"]:
                if not new_value.strip().isdigit():
                    print("Must be a number.")
                    continue
                new_value = int(new_value)
            _set_by_path(phone, path, new_value)


def delete_phone(phones: PhoneList):
    if not phones:
        print("No phones to delete.\n")
        return
    while True:
        idx = questionary.select(
            "Select phone to delete:", choices=_phone_choices(phones)).ask()
        if idx == "-1":
            break
        phones.pop(idx)


def save_data(phones: PhoneList):
    with open(PHONES_JSON_PATH, "w") as file:
        json.dump(phones, file, indent=4)
    sys.exit()


ACTIONS = {
    "DISPLAY": display_phones,
    "ADD": add_phone,
    "EDIT": edit_phone,
    "DELETE": delete_phone,
    "SAVE": save_data
}


def main():
    path = PHONES_JSON_PATH
    phones: PhoneList = json.loads(path.read_text()) if path.exists() else []
    while True:
        answer = questionary.select(
            "What would you like to do?", choices=MAIN_MENU).ask()
        if answer is None or answer == "EXIT":
            sys.exit()
        if answer in ACTIONS:
            ACTIONS[answer](phones)


main()
