# Enter your code here. Read input from STDIN. Print output to STDOUT

v = int(raw_input())
n = int(raw_input())
ar = [int(i) for i in raw_input().split()]

for j in range(n):
    if ar[j] == v:
        print j
        break