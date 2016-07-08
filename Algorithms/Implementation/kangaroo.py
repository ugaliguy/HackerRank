# Python 2

#!/bin/python

import sys


x1,v1,x2,v2 = [int(i) for i in raw_input().split()]

if v1 == v2:
    print 'NO'
elif v2 > v1:
    print 'NO' # Since x1 < x2
elif v1 > v2:
    time = 1.0*(x1 - x2)/(v2 - v1)
    if time > 0 and time.is_integer():
        print 'YES'
    else:
        print 'NO'
