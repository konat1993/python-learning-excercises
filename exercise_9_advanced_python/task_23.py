# Task 23: Format the current date and time using f-strings.

from datetime import datetime as dt

now = dt.now()

print(f"{now:%Y/%m/%d %H:%M:%S}")
