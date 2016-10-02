#!/bin/python
def insertionSort(ar):
    e = ar[m-1]
    pos = m-2
    while ar[pos] > e and pos>=0:
        ar[pos+1] = ar[pos]
        pos -= 1
        print " ".join(str(ch) for ch in ar)
    ar[pos+1] = e
    print " ".join(str(ch) for ch in ar)  

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
