# Python 2

import sys


def new_years_queue(q):
    last = len(q) - 1
    swaps = 0
    swapped = False
    for i,p in enumerate(q):
        if p - 1 - i > 2:
            return 'Too chaotic'

    for j in range(last):
        for k in range(last):
            if q[k] > q[k+1]:
                q[k],q[k+1] = q[k+1],q[k]
                swaps += 1
                swapped = True
                
        if swapped:
            swapped = False
        else:
            break
    return swaps

t = int(raw_input().strip())
for i in xrange(t):
    n = int(raw_input())
    q = [int(j) for j in raw_input().split()]
    # your code goes here
    print new_years_queue(q)
        