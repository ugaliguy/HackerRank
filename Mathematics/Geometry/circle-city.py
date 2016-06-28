# Python 2

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math


t = int(raw_input())

for i in range(t):
    d,k = [int(j) for j in raw_input().split()]
    rt = math.sqrt(d)
    ceiling = int(math.ceil(rt))
    count = 0
    for p in range(ceiling):
        if (math.sqrt(d - p**2).is_integer()):
            count += 4
        if count > k:
            answer = 'impossible'
        else:
            answer = 'possible'
    print answer
        