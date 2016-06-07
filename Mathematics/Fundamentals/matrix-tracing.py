# Python 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Use Fermat's Little Theorem
# The Brute Force approach is way too slow

mod = 10**9 + 7

def fact_mod(a):
  answer = 1
  for i in range(1,a):
    answer =((answer%mod)*((i+1)%mod))%mod
  return answer

def powermod(a,b):
  if b==0:
    return 1
  if b == 1:
    return a
  temp = powermod(a,b/2)
  if b%2==0:
    return ((temp%mod)**2)%mod
  else:
    return (a*((temp%mod)**2))%mod

def inversemod(a):
  return powermod(a,mod-2)

t = int(raw_input())

for i in range(t):
    n,m = [int(x) for x in raw_input().split()]
    num = 1
    den = 1
    for i in range(1, n+m-1):
    	num = ((num%mod)*(i%mod))%mod
    for i in range(1, n):
    	den = ((den%mod)*(i%mod))%mod
    for i in range(1, m):
    	den = ((den%mod)*(i%mod))%mod
    answer = ((num%mod)*(inversemod(den)%mod))%mod
    print answer