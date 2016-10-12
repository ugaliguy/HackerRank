def count(n, memo):
    if n <= 0:
        return 0
    elif n <=2:
        return n
    elif n == 3:
        return 4
    
    if memo[n]==0:
        memo[n] = count(n-3,memo) + count(n-2,memo) + count(n-1,memo)
    return memo[n]

def stairs(n):
    memo = [0]*(n+1)
    return count(n,memo)

s = int(raw_input().strip())
for a0 in xrange(s):
    n = int(raw_input().strip())
    print stairs(n)
