# Python 2

#!/bin/python

import sys


n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]

if n >= m:
    print n-m
else:
    print n-(m%n)