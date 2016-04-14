# Enter your code here. Read input from STDIN. Print output to STDOUT

m = int(raw_input())
a = raw_input().split()
a_int = list(map(int, a))
a_set = set(a_int)

n = int(raw_input())
b = raw_input().split()
b_int = list(map(int, b))
b_set = set(b_int)

symm_diff = a_set.difference(b_set).union(b_set.difference(a_set))

symm_diff_list = sorted(list(symm_diff))

for i in symm_diff_list:
	print i