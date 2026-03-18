# Task 13: Randomly split a list of participants into two teams
# and save results to a text file.


import random


people_group = [
    "Anna",
    "John",
    "Terry",
    "Martha",
    "Joe",
    "Claudia",
    "Luke",
    "Paul",
    "Tom",
    "Bob"
]

shuffled_people = random.sample(people_group, k=10)

team_1 = []
team_2 = []

for idx, person in enumerate(shuffled_people):
    if idx < int(len(people_group) / 2):
        team_1.append(person)
    else:
        team_2.append(person)

print(
    f"Team 1: {team_1}"
)
print("==========================" * 2)
print(
    f"Team 2: {team_2}"
)
