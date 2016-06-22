# Python 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    answer = (n**2)%((10**9) + 7)
    print answer