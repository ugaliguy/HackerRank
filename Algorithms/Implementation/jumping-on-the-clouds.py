#!/bin/python

import sys


n = int(raw_input().strip())
c =[int(i) for i in raw_input().strip().split(' ')]

jumps = 0
i = 0

while(i < len(c) - 2):
    if c[i+2] == 0:
        jumps += 1
        i += 2
    else:
        jumps += 1
        i += 1
if i == len(c) - 2:
    jumps += 1
    
print jumps