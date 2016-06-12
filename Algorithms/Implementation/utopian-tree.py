# Python 2

#!/bin/python

import sys

def utopian(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    elif n % 2 == 1:
        return 2*utopian(n-1)
    return utopian(n-1) +1

t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    h = utopian(n)
    print h