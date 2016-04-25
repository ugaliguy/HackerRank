# Use Python 3
# Still figuring out how to do this in Python 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

from datetime import datetime

t = int(input())

for i in range(t):
    time_1 = datetime.strptime(input(), "%a %d %b %Y %X %z")
    time_2 = datetime.strptime(input(), "%a %d %b %Y %X %z")
    result = abs(int((time_1 - time_2).total_seconds()))
    print(result)