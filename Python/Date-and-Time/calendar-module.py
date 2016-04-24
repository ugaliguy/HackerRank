# Enter your code here. Read input from STDIN. Print output to STDOUT

import calendar

month, day, year = map(int, raw_input().split())

input_date = calendar.weekday(year, month, day)

print calendar.day_name[input_date].upper()