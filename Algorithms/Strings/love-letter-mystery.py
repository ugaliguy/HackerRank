# Enter your c# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(raw_input())

for case in range(t):
    s = raw_input().strip()
    reduction = 0
    for i in range(len(s)//2):
        reduction += abs(ord(s[i]) - ord(s[-1-i]))
    print reduction