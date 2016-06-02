import sys

time = input().strip()
meridiem = time[-2:]
hour = int(time[0:2])
answer = time
if meridiem == 'PM' and hour < 12:
    hour = (hour + 12)%24
    time = str(hour) + time[2:-2]
elif meridiem == 'AM' and hour == 12:
    time = '00' + time[2:-2]
else:
    time = time[:-2]

print(time)