# Enter your code here. Read input from STDIN. Print output to STDOUT

t  = int(raw_input())

for i in range(t):
    s = raw_input().strip()
    rvs = s[::-1]
    n = len(s)
    for i in range(1,n):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(rvs[i]) - ord(rvs[i-1])):
            print 'Not Funny'
            break
    else:
        print 'Funny'
        