# Python 2

#!/bin/python

import sys


t = int(raw_input())
for i in xrange(t):
    n,k = [int(j) for j in raw_input().split()]
    a = map(int,raw_input().split())
    count = 0
    for i in a:
        if i <= 0:
            count += 1
    if count >=k:
        print "NO"
    else:
        print "YES"