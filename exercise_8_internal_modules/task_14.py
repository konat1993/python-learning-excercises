# Task 14: List all files in a given folder with their sizes
# using the pathlib module.


from pathlib import Path


current_directory = Path(__file__).parent


def format_size(size_bytes):
    units = ["B", "KB", "MB", "GB"]
    size = float(size_bytes)
    unit_index = 0
    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024
        unit_index += 1
    return f"{size:.2f} {units[unit_index]}"


for item in current_directory.iterdir():
    if item.is_file():
        size_bytes = item.stat().st_size
        print(f"{item.name} (Size: {format_size(size_bytes)})")
