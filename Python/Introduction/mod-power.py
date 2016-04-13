# Enter your code here. Read input from STDIN. Print output to STDOUT

# __future__ allows Python 3 functionality in Python 2 code
from __future__ import division 

a = int(raw_input())
b = int(raw_input())
m = int(raw_input())

power = a**b
modulus = (a**b)%m

print power
print modulus