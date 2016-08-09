# Python 2

#!/bin/python

import sys


n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))

count = 0
sides = sum(a)
for i in range(n):
	if a[i] >= sides/2:
		count += 1
    
print count
