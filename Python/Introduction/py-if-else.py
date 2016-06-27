# Python 2

import sys


n = int(raw_input())

if (n%2 == 1) or (n%2 == 0 and n >= 6 and n <= 20):
	print "Weird"
else:
	print "Not Weird"