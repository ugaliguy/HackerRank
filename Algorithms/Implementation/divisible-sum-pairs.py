# Python 2

#!/bin/python

import sys


n,k = [int(i) for i in raw_input().split()]
a = [int(j) for j in raw_input().split()]

count = 0
for p in range(n):
    for q in range(p+1,n):
        pair = a[p] + a[q]
        if pair%k == 0:
            count += 1
print count
