# Python 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

import math


t = int(raw_input())

for i in range(t):
    n,m = [int(x) for x in raw_input().split()]
    symbols = n + m - 1
    answer = (math.factorial(symbols)/(math.factorial(n)*math.factorial(m-1)))%((10**9) + 7)
    print answer