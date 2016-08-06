# Python 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(raw_input())

for case in range(t):
    a,p = [int(i) for i in raw_input().split()]

    if (pow(a,(p-1)/2,p) == 1) or (a == 0) or (a == 2):
        print "YES"
    else:
        print "NO"