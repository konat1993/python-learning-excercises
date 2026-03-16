# Task 1: Create program that will manage a video library.
# Options that should be in it:
# 1. Displaying information about films (title, name and surname of the director, year of release)
# 2. Adding films
# 3. Editing films
# 4. Deleting films
# 5. Searching for films by title
# All data is stored in a CSV file

import sys
from pathlib import Path
import csv
from typing import TypedDict

import questionary

VIDEO_LIBRARY_PATH = Path(__file__).parent / "video_library.csv"
FIELDNAMES = ["title", "director_full_name", "publish_year"]

MAIN_MENU = [
    {"name": "See video items", "value": "SEE"},
    {"name": "Add video", "value": "ADD"},
    {"name": "Edit video list item", "value": "EDIT"},
    {"name": "Delete video item", "value": "DELETE"},
    {"name": "Search video items by title", "value": "SEARCH"},
    {"name": "Exit", "value": "EXIT"},
]


class VideoItem(TypedDict):
    title: str
    director_full_name: str
    publish_year: str


def get_video_items() -> list[VideoItem]:
    # Get
    if not VIDEO_LIBRARY_PATH.exists():
        return []
    with open(VIDEO_LIBRARY_PATH, encoding="utf-8") as file:
        return list(csv.DictReader(file))


def save_videos(videos: list[VideoItem]) -> None:
    # Update / Delete
    with open(VIDEO_LIBRARY_PATH, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(videos)


def add_video(item: VideoItem) -> None:
    # Create
    write_header = not VIDEO_LIBRARY_PATH.exists()
    with open(VIDEO_LIBRARY_PATH, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        if write_header:
            writer.writeheader()
        writer.writerow(item)


def format_video_list(videos: list[VideoItem]) -> list[str]:
    return [
        f"{i}. {v['title']} ({v['publish_year']}) by {v['director_full_name']}"
        for i, v in enumerate(videos, start=1)
    ]


def run_see() -> None:
    videos = get_video_items()
    if not videos:
        print("No videos yet. Add one first.")
        return
    for line in format_video_list(videos):
        print(line)


def run_add() -> None:
    item: VideoItem = {
        "title": questionary.text("Title:").ask() or "",
        "director_full_name": questionary.text("Director full name:").ask() or "",
        "publish_year": questionary.text("Publish year:").ask() or "",
    }
    add_video(item)
    print("Added.")


def run_edit() -> None:
    videos = get_video_items()
    if not videos:
        print("No videos to edit. Add one first.")
        return
    choices = format_video_list(videos) + ["Exit"]
    while True:
        choice = questionary.select(
            "Which item would you like to update?", choices=choices).ask()
        if choice is None or choice == "Exit":
            break
        idx = choices.index(choice)
        if idx >= len(videos):
            break
        video = videos[idx]
        field_choices = [
            {"name": f"Title: {video['title']}", "value": "title"},
            {"name": f"Director: {video['director_full_name']}",
                "value": "director_full_name"},
            {"name": f"Publish year: {video['publish_year']}",
                "value": "publish_year"},
            {"name": "Exit", "value": "Exit"},
        ]
        while True:
            field = questionary.select(
                "Which part to change?", choices=field_choices).ask()
            if field is None or field == "Exit":
                break
            new_val = questionary.text(
                f"New {field}:", default=video[field]).ask()
            if new_val is not None:
                videos[idx][field] = new_val
                save_videos(videos)


def run_delete() -> None:
    while True:
        videos = get_video_items()
        if not videos:
            print("No items to delete. Add one first.")
            return
        choices = format_video_list(videos) + ["Exit"]
        choice = questionary.select(
            "Which item would you like to delete?", choices=choices).ask()
        if choice is None or choice == "Exit":
            break
        idx = choices.index(choice)
        if idx < len(videos):
            videos.pop(idx)
            save_videos(videos)


def run_search() -> None:
    videos = get_video_items()
    if not videos:
        print("No videos to search. Add one first.")
        return
    phrase = questionary.text("Enter a phrase: ").ask() or ""
    phrase = phrase.lower().strip()
    found = [v for v in videos if phrase in v["title"].lower()]
    if not found:
        print("No items found.")
    else:
        for line in format_video_list(found):
            print(line)


ACTIONS = {
    "SEE": run_see,
    "ADD": run_add,
    "EDIT": run_edit,
    "DELETE": run_delete,
    "SEARCH": run_search,
}


def main() -> None:
    while True:
        answer = questionary.select(
            "What would you like to do?", choices=MAIN_MENU).ask()
        print(answer)
        if answer is None or answer == "EXIT":
            sys.exit()
        if answer in ACTIONS:
            ACTIONS[answer]()


main()
