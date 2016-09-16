#!/bin/python

def print_arr(a):
    string = ''
    for i in range(len(a)):
        string += str(a[i])
        if (i < len(a) -1):
            string += ' '
    print string  

def insertion_sort(ar):    
    for i in range(1,s):
        for j in range(i):
            if (ar[i-j] < ar[i-j-1]):# if(ar[i]<ar[j])
                t = ar[i-j]			 # t=ar[i]
                ar[i-j] = ar[i-j-1]	 # ar[i]=ar[j]
                ar[i-j-1] = t		 # ar[j]=t
        print_arr(ar)

s = int(raw_input())
ar = [int(i) for i in raw_input().strip().split()]
insertion_sort(ar)
