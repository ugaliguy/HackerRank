# Python 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(raw_input())

for i in range(t):
    n,m,s = [int(j) for j in raw_input().split()]
    last = (s + m - 2)%n + 1
    print last