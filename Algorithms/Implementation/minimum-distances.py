# Python 2

#!/bin/python

import sys


n = int(raw_input())
a = map(int,raw_input().split())
distances = []
for i in range(n):
    for j in range(i+1,n):
        if i != j and a[i] == a[j]:
            dist = abs(i - j)
            distances.append(dist)
if len(distances) > 0:
    print min(distances)
else:
    print -1