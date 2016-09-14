#!/bin/python

import sys


s = raw_input().strip()
n = long(raw_input().strip())

numb_a = s.count('a')
quot = n/len(s)
rem = n%len(s)
answer = quot*numb_a + s[0:rem].count('a')
print answer
