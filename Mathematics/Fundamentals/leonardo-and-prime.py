leonardo-and-prime.py

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def factor(n):
    if n <= 1:  return [ ]
    d = 2
    factors = [ ]
    while n >= d*d:
        if n % d == 0:
            factors.append(d)
            n = n/d
        else:
            d += 1 + (d%2)  # 2 -> 3, odd -> odd + 2
    factors.append(n)
    return factors

# The following is a list of the first 25 primes (whose product is > 10**20)
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]


q = int(raw_input())

for i in range(q):
    n = int(raw_input())
    count = 0
    product = primes[0]
    i = 0
    if n == 1:
        count = 0
    elif n <= 3:
        count = 1
    else:
        while product <= n:
            count += 1
            i += 1
            product *= primes[i]
   
    print count