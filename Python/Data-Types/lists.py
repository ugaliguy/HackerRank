# __future__ allows Python 3 functionality in Python 2 code
from __future__ import print_function 

arr = []

n = int(raw_input())

for i in range(0,n):
	ops = raw_input().split()

	if ops[0] == "append":
		arr.append(int(ops[1]))
	elif ops[0] == "insert":
		arr.insert(int(ops[1]), int(ops[2]))
	elif ops[0] == "remove":
		arr.remove(int(ops[1]))
	elif ops[0] == "pop":
		arr.pop()
	elif ops[0] == "index":
		arr.index(int(ops[1]))
	elif ops[0] == "count":
		arr.count(int(ops[1]))
	elif ops[0] == "sort":
		arr.sort()
	elif ops[0] == "reverse":
		arr.reverse()
	elif ops[0] == "print":
		print(arr)