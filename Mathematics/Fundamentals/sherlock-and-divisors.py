# Python 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    limit = int(math.sqrt(n))
    div  = 0
    i = 1
    while(i <= limit):
        if (n%i == 0):
            if (i%2 == 0 and (n/i)%2 == 0):
                if (i == n/i):
                    div += 1
                else:
                    div += 2
            elif (i%2 == 0 or (n/i)%2 == 0):
                div += 1
        i += 1
    print div