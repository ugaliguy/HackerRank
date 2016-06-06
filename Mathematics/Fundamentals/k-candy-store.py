# Python 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

import math


t = int(raw_input())

for i in range(t):
	n = int(raw_input())
	k = int(raw_input())
	answer = (math.factorial(n+k-1)/(math.factorial(n-1)*math.factorial(k)))%(10**9)
	print answer