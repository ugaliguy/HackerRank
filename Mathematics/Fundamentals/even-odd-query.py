# Python 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

def find(x,y):
	answer = 1
	if x > y:
		return 1
	else:
		answer = a[x]**find(x+1,y)
		return answer

n = int(raw_input())
a = [int(x) for x in raw_input().split()]
q = int(raw_input())
for i in range(q):
    x,y = [int(z) for z in raw_input().split()]
    if x > y:
        print 'Odd'
    else :
        if a[x-1]%2 == 0:
            if y != x and x < n:
                if a[x] != 0:
                    print 'Even'
                else:
                    print 'Odd'
            else:
                if a[x-1]%2 == 0:
                    print 'Even'
                else:
                    print 'Odd'
        else:
            print 'Odd'