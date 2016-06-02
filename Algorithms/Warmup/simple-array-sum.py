import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
answer = 0
for i in arr:
    answer += i
    
print(answer)