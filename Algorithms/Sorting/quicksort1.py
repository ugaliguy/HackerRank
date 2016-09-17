#!/bin/python
def partition(ar):   
    p = ar[0]
    left = []
    equal = []
    right = []
    for i in ar:
        if i < p:
            left.append(i)
        elif i == p:
            equal.append(i)
        else:
            right.append(i)
    result = left + equal + right
    for j in result:
        print str(j) + ' ',
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)
