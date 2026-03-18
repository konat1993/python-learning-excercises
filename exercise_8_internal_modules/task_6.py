# Task 6: Convert a string in "DD-MM-YYYY" format to datetime and print it as "YYYY/MM/DD".

from datetime import datetime

initial_date = "14-08-2013"

format_date = datetime.strptime(
    initial_date,
    '%d-%m-%Y'
).strftime("%Y/%m/%d")

print(format_date)
