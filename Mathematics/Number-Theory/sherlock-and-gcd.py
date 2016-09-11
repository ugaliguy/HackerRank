# Enter your code here. Read input from STDIN. Print output to STDOUT

def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)
    
def multi_gcd(numbers):
    return reduce(lambda x,y: gcd(x,y), numbers)

t = int(raw_input())

for i in range(t):
    n = int(raw_input())
    arr = [int(j) for j in raw_input().split()]
    if (len(arr) < 2):
        print "NO"
    elif multi_gcd(arr) == 1:
        print "YES"
    else:
        print "NO"