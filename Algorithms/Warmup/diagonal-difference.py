import sys

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

diag = 0
anti = 0
for i in range(n):
    diag += a[i][i]
    anti += a[i][n-i-1]

answer = abs(diag - anti)
print(answer)