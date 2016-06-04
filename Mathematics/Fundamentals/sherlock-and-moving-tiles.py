# Python 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

length, velocity1, velocity2 = raw_input().split()
queries = int(raw_input())
for q in range(queries):
    area = int(raw_input())
    time = math.sqrt(2)*(int(length) - math.sqrt(area))/abs(int(velocity1) - int(velocity2))
    answer = format(time, '.20f') # This was needed pass Test Case #4
    print answer