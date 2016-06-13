# Python 2

#!/bin/python

import sys


t = int(raw_input())
for i in range(t):
    n,c,m = [int(j) for j in raw_input().split()]
    wrappers = n/c
    count = wrappers
    while(wrappers >= m):
        wrappers -= m
        count += 1
        wrappers += 1
    print count