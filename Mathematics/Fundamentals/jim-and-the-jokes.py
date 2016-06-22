# Python 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

def base(m,d): # Converts d (base m) to its decimal equivalent
    result = 0
    c = 1
    while(d > 0):
        x = d%10
        if(x >= m):
            return -1
        d /= 10
        result += x*c
        c *= m
    return result

n = int(raw_input())
decimals = [0]*37 # 37 = 12*3 + 1 = max(base(i,j)) for 1<=i<=12 (months) and 1<=j<=31 (days)
for i in range(n):
    m,d = [int(j) for j in raw_input().split()]
    x = base(m,d)
    result = 0
    if(x != -1):
        result += decimals[x]
        decimals[x] += 1
        
print result