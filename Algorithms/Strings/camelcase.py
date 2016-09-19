#!/bin/python

import sys


s = raw_input().strip()

count = 0
if len(s) > 0:
    count = 1
for i in xrange(1, len(s)):
    if ord(s[i]) >= ord('A') and ord(s[i]) <= ord('Z'):
        count += 1
print count 
