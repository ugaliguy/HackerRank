# Python 2 

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Observation: If you factor 9 from 9, 90, 99, 900, 909, 990, 999, ...
# you ge the binary numbers 1, 10, 11, 100, 101, 110, 111,  ...

t = int(raw_input())

for i in range(t):
    n = int(raw_input())
    j = 1
    while(int(str(bin(j))[2:].replace('1','9'))%n!=0):
        j += 1
    d = str(bin(j))[2:].replace('1','9')
    print d