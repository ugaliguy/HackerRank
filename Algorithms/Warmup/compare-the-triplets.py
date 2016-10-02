#!/bin/python

import sys


a = [int(i) for i in raw_input().strip().split(' ')]
b = [int(i) for i in raw_input().strip().split(' ')]

alice = 0
bob = 0

for i in range(3):
    if a[i] > b[i]:
        alice += 1
    elif a[i] < b[i]:
        bob += 1
        
print str(alice) + ' ' + str(bob)
