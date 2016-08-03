halloween-party.py

# Python 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(raw_input())

for i in range(t):
    k = int(raw_input())
    l = 0
    w = 0
    if k%2 == 1:
        l = k/2 + 1
        w = k - l
    else:
        l = k/2
        w = k/2
    answer = l*w
    print answer