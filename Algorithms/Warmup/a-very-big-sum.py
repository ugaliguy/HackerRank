# You are given an array of integers of size . You need to print the sum of 
# the elements in the array, keeping in mind that some of those integers may be quite large.

# Note there is nothing different in this code from simple-array-sum.py
# Python can handle big numbers

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
answer = 0
for i in arr:
    answer += i
    
print(answer)