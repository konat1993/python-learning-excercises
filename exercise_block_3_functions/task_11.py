# Task 11: Write a function that takes a day-of-week number and returns the name of that day using match/case.

def get_day_name(weekday_number: int) -> str:
    match weekday_number:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "weekday_number must be in range 1–7"


for i in range(1, 9):
    print(i, get_day_name(i))
