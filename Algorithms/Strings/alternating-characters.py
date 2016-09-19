# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(raw_input())

for i in range(t):
    s = raw_input().strip()
    n = len(s)
    count = 0
    for i in range(1,n):
        if s[i] == s[i-1]:
            count += 1
    print count