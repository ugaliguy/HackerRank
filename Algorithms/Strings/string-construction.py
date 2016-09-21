#!/bin/python

import sys


n = int(raw_input().strip())
for a0 in xrange(n):
    s = raw_input().strip()
    p =''
    cost = 0
    letters = set()
    for i in s:
        if i not in letters:
            cost += 1
            letters.add(i)
    print cost
