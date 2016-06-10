# Python 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

def gcd(m,n):
	while(n):
		m,n = n, m%n
	return m

t = int(raw_input())
for i in range(t):
    a,b,c = [int(x) for x in raw_input().split()]
    
    d = gcd(a,b)
    
    if (c%d == 0) and (a >= c or b >= c):
        print "YES"
    else:
        print "NO"