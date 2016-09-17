#!/bin/python

def quick_sort(ar):
    if len(ar) < 2:
        return ar
    else:
        p = ar[0]
        left = []
        right = [] 
        equal = []
        for i in ar:
            if i < p:
                left.append(i)
            elif i == p:
                equal.append(i)
            else:
                right.append(i)
            
        left_sort = quick_sort(left)
        right_sort = quick_sort(right)
        ar_sort = left_sort + equal + right_sort
        print ' '.join([str(x) for x in ar_sort])
        return ar_sort
        

m = input()
ar = [int(i) for i in raw_input().strip().split()]
quick_sort(ar)
