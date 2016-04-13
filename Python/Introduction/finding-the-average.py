# Enter your code here. Read input from STDIN. Print output to STDOUT

# __future__ allows Python 3 functionality in Python 2 code
from __future__ import division 

n = int(raw_input())

records = {}

for i in range(0,n):
	record = raw_input().split()
	student = record[0]
	math = record[1]
	physics = record[2]
	chemistry = record[3]
	records[student] = [math, physics, chemistry]

name = raw_input()

average = (float(records[name][0]) + float(records[name][1]) + float(records[name][2]))/3

print "%.2f" % average # Note how we round to two decimal places