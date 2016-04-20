# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

[string, n] = list(raw_input().split())
string = sorted(string)
n = int(n)

for k in range(1, n + 1):
    combs = sorted(list(combinations(string, int(k))))
    for comb in combs:
        print ''.join(comb)