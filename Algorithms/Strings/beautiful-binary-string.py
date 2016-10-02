#!/bin/python

import sys


n = int(raw_input().strip())
b = raw_input().strip()
chb = [int(c) for c in b]

count = 0
for i in range(2,n):
    if chb[i-2:i+1] == [0,1,0]:
        chb[i] = 1
        count += 1
print count
