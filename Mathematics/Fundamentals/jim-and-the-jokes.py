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
decimals = [0]*38 # 37 = 12*3 + 1 = max(base(i,j)) for 1<=i<=12 (months) and 1<=j<=31 (days)
for i in range(n):
    m,d = [int(j) for j in raw_input().split()]
    x = base(m,d)
    #print 'x = ' + str(x)
    if(x != -1):
        decimals[x] += 1

answer = 0
for j in decimals:
    # Note that the following if-else  is necessary in order
    # to deal with large integers
    if j%2 == 0:
        answer += (j/2)*(j-1)
    else:
        answer += ((j-1)/2)*j
        
print answer 