# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

length = int(raw_input())
string = raw_input().split()
numb_ind = int(raw_input())

count = 0.0 # We want the answer to be a float

combs = sorted(list(combinations(string, numb_ind)))

for comb in combs:
    if 'a' in comb:
        count += 1
        
print count/len(combs)