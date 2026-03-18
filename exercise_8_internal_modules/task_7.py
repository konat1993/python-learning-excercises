# Task 7: Calculate the number of days between two given dates.

from datetime import datetime

date1 = datetime(2026, 3, 17)
date2 = datetime(2026, 4, 16)
# date2 = datetime.now()

print(
    f"The number of days between {date1.strftime('%Y/%m/%d')} and {date2.strftime('%Y/%m/%d')} is {(date2 - date1).days}"
)
