# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = map(int, raw_input().split())

d = defaultdict(list)
b_list = []

for i in range(n):
	d[raw_input()].append(i + 1)

for j in range(m):
	b_list.append(raw_input())

for element in b_list:
	if element in d.keys():
		print ' '.join(map(str, d[element]))
	else:
		print -1