# Python 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

t = int(raw_input())

for case in range(t):
    a,b,x = [int(i) for i in raw_input().split()]
    n = int(math.floor((a**b)/x))
    possible = [(n-1)*x,n*x,(n+1)*x]
    distances = [int(abs(possible[j] - a**b)) for j in range(3)]
    mindx = distances.index(min(distances))
    print possible[mindx]