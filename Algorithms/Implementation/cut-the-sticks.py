# Python 2

#!/bin/python

import sys


n = int(raw_input())
arr = map(int,raw_input().split())
arr.sort()
count = len(arr)
while(count >= 1):
    print count
    min = arr[0]
    for i in range(count):
        if arr[0] == min:
            arr.pop(0)
        count = len(arr)