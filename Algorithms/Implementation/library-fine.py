# Python 2

import sys


def fine(d1,m1,y1,d2,m2,y2):
    d = d1 - d2
    m = m1 - m2
    y = y1 - y2
    if y > 0:
        return 10000
    elif m > 0  and y == 0:
        return m*500
    elif d > 0 and y == 0 and m == 0:
        return d*15
    else:
        return 0
    
d1,m1,y1 = [int(i) for i in raw_input().split()]
d2,m2,y2 = [int(j) for j in raw_input().split()]

print fine(d1,m1,y1,d2,m2,y2)