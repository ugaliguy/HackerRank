# Python 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

def gcd(m,n):
	while(n):
		m,n = n, m%n
	return m

t = int(raw_input())
for i in range(t):
    l,b = raw_input().split()
    l = int(l)
    b = int(b)
    g = gcd(l,b)
    p = l*b
    answer = p/(g**2)
    print str(answer)