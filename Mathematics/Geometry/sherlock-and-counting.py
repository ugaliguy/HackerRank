# Python 2

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

t = int(raw_input())
for i in range(t):
    n,k = [int(j) for j in raw_input().split()]
    discriminant = n**2 - 4*n*k
    answer = 0
    if n <= 4*k:
        answer = n-1
    else:
        root_max = (n + math.sqrt(discriminant))/2
        root_min = (n - math.sqrt(discriminant))/2
        answer = int(root_min) + int(n - root_max)
    print answer
        