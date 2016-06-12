# Python 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

t = int(raw_input())

for i in range(t):
    a,b = [int(j) for j in raw_input().split()]
    root_a = math.sqrt(a)
    root_b = math.sqrt(b)
    answer = int(math.floor(root_b)) - int(math.ceil(root_a)) + 1
    print answer