#!/bin/python

import sys
t = int(raw_input().strip())

size = 3 
while True:
    if t <= size:
        print size - (t-1)
        break
    else:
        t -= size
        size *= 2
