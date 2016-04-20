# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

[string, n] = list(raw_input().split())

perms = sorted(list(permutations(string, int(n))))

for perm in perms:
    print ''.join(perm)