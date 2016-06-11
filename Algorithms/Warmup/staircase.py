import sys

n = int(input().strip())

for i in range(n):
    space = ' '*(n-i-1)
    pound = '#'*(i + 1) 
    print(space + pound)