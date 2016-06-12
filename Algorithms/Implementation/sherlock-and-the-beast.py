# Python 2

#!/bin/python


import sys

t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    decent = []
    for j in reversed(range(n+1)):
        i = n-j
        if (j == n) and (j%3 == 0):
            decent = ['5']*j
            break
        elif (i == n) and (i%5 == 0):
            decent = ['3']*i
            break
        elif (j%3 == 0) and (i%5 == 0):
            decent = ['5']*j + ['3']*i
            break
        else:
            decent = ['-1']
   
    decent = int(''.join(decent))
    print decent