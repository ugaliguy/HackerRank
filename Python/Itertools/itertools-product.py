# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

a = map(int, raw_input().split())
b = map(int, raw_input().split())

prod = list(product(a,b))

print(' '.join(map(str,prod)))