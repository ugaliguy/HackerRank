# Python 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def is_sqrt(n):
    if (math.sqrt(n) - int(math.sqrt(n))):
        return False
    else:
        return True
    
t = int(raw_input())

for i in range(t):
    n = int(raw_input())
    if is_sqrt(5*n**2 + 4) or is_sqrt(5*n**2 - 4): # Take advantage of Binet's Formula
        print "IsFibo"
    else:
        print "IsNotFibo"