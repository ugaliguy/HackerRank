# Python 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    answer = ((2**n) - 1)%(10**5) # Modulo to deal with large integers
    print answer