# Python 2

#!/bin/python

import sys


n,t = [int(k) for k in raw_input().split()]
width = map(int,raw_input().split())
for r in range(t):
    i,j = [int(k) for k in raw_input().split()]
    print min(width[i:j+1])