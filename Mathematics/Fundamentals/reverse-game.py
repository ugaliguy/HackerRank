# Python 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(raw_input())
for i in range(t):
    n,k = [int(x) for x in raw_input().split()]
    if(k>=n/2):
        print(2*(n-k-1))
    else:
        print(2*k+1)