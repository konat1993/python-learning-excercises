# Task 19: Load CSV with day, min/max temp, precipitation;
# show extremes, averages, wettest day, rainy days.

import csv
from pathlib import Path
from statistics import mean


WEATHER_CSV_PATH = Path(__file__).parent / "task_19.csv"

if not WEATHER_CSV_PATH.exists():
    raise SystemExit(f"Weather CSV file does not exist: {WEATHER_CSV_PATH}")

try:
    with open(WEATHER_CSV_PATH) as file:
        weather_data = list(csv.DictReader(file, skipinitialspace=True))
except OSError as exc:
    raise SystemExit(f"Failed to read weather CSV file: {exc}") from exc

for item in weather_data:
    item["min_temp"] = float(item["min_temp"])
    item["max_temp"] = float(item["max_temp"])
    item["precipitation"] = float(item["precipitation"])

lowest_temp_item = min(weather_data, key=lambda x: x["min_temp"])
highest_temp_item = max(weather_data, key=lambda x: x["max_temp"])
avg_min_temp = mean(item["min_temp"] for item in weather_data)
avg_max_temp = mean(item["max_temp"] for item in weather_data)
highest_precipitation_item = max(
    weather_data, key=lambda x: x["precipitation"]
)
rainy_days = [
    item["day"]
    for item in weather_data
    if item["precipitation"] > 0
]

print(f"Day with the lowest temp: {lowest_temp_item['day']}")
print(f"Day with the highest temp: {highest_temp_item['day']}")
print(f"Average minimum temperature: {avg_min_temp:.1f}")
print(f"Average maximum temperature: {avg_max_temp:.1f}")
print(
    f"Wettest day: {highest_precipitation_item['day']} "
    f"({highest_precipitation_item['precipitation']})"
)

print("Rainy days: ")
for day in rainy_days:
    print(day)
