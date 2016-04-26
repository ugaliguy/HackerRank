# This does not pass all tests on Hackerrank
# Fix this code -  for Python 2

# Enter your code here. Read input from STDIN. Print output to STDOUT
from datetime import datetime

t = int(raw_input())

for i in range(t):
    time_1_arr = raw_input().split()
    time_1 = ' '.join(time_1_arr[:5])
    time_1 = datetime.strptime(time_1, "%a %d %b %Y %X")

    time_2_arr = raw_input().split()
    time_2 = ' '.join(time_2_arr[:5])
    time_2 = datetime.strptime(time_2, "%a %d %b %Y %X")
    
    tz_1 = abs(int(time_1_arr[5])/100)*3600 + (int(time_1_arr[5])%100)*60
    if int(time_1_arr[5]) < 0:
        tz_1 = -tz_1
    
    tz_2 = abs(int(time_2_arr[5])/100)*3600 + (int(time_2_arr[5])%100)*60
    if int(time_2_arr[5]) < 0:
        tz_2 = -tz_2

    #print 'tz_1: ' + str(tz_1)
    #print 'tz_2: ' + str(tz_2)
    #print '***************************'
    sign = int(time_1_arr[5])*int(time_2_arr[5])
    if sign >= 0:
        diff = abs(int((time_1 - time_2).total_seconds()) - abs(tz_1 - tz_2))
    else:
        diff = abs(int((time_1 - time_2).total_seconds()) + abs(tz_1 - tz_2))
    print diff