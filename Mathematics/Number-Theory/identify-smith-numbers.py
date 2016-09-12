# Enter your code here. Read input from STDIN. Print output to STDOUT

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

n = int(raw_input())

digits = list(str(n))
sum_digits = 0
for digit in digits:
    sum_digits += int(digit)
    
factors = factor(n)
factors_digits = [0]
for fact in factors:
    factors_digits += list(str(fact))
# print "factors_digits = " + str(factors_digits)
sum_factors = 0
for digit in factors_digits:
    sum_factors += int(digit)
    
if sum_digits == sum_factors:
    print 1
else:
    print 0
