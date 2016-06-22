# Enter your code here. Read input from STDIN. Print output to STDOUT

def gcd(m,n):
	while(n):
		m,n = n, m%n
	return m

t = int(raw_input())
for i in range(t):
    x1,y1,x2,y2 = [int(j) for j in raw_input().split()]
    answer = 0
    
    diffx = abs(x1 - x2)
    diffy = abs(y1 - y2)
    if (x1 == x2):
        answer = diffy -1
    elif (y1 == y2):
        answer = diffx -1
    else:
        answer = gcd(diffx,diffy) - 1
    print answer
