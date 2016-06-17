# Python 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(raw_input())

for i in range(t):
    n = int(raw_input())
    a = int(raw_input())
    b = int(raw_input())
    
    c = min(a,b)
    d = max(a,b)
    last = []
    for i in range(n):
        last.append(i*c + (n-1-i)*d)
    last = set(last)
    print ' '.join(str(x) for x in list(sorted(list(last))))