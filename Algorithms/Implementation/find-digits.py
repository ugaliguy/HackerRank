# Python 2

#!/bin/python

import sys


t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    digits = [int(j) for j in list(str(n))]
    count = 0
    for d in digits:
        if (d != 0) and (n%d == 0):
            count += 1
    print count