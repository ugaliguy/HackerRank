# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

[string, n] = list(raw_input().split())
string = sorted(string)
n = int(n)

combs = sorted(list(combinations_with_replacement(string, n)))
for comb in combs:
    print ''.join(comb)