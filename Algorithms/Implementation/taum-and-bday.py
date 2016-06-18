# Python 2

import sys


t = int(raw_input())
for i in range(t):
    b,w = [int(j) for j in raw_input().split()]
    x,y,z = [int(k) for k in raw_input().split()]
    cost = min(b*x, b*(y+z)) + min(w*(x+z),w*y)
    print cost
