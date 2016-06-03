# Python 2

# Adam is standing at point (a,b) in an infinite 2D grid. 
# He wants to know if he can reach point (x,y) or not. 
# The only operation he can do is to move to point (a+b,b), (a,a+b), (a-b,b), or (a,a-b) 
# from some point (a,b). 
# It is given that he can move to any point on this 2D grid, 
# i.e. the points having positive or negative X (or Y) co-ordinates.

# Enter your code here. Read input from STDIN. Print output to STDOUT

def gcd(m,n):
	while(n):
		m,n = n, m%n
	return m

t = int(raw_input())
for i in range(t):
    a,b,x,y = raw_input().split()
    if gcd(int(a),int(b)) == gcd(int(x),int(y)):
        print 'YES'
    else:
        print 'NO'