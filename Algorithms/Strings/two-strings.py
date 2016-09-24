# Enter your code here. Read input from STDIN. Print output to STDOUT

p = int(raw_input())

for pair in range(p):
    a = raw_input().strip()
    b = raw_input().strip()
    sa = set(a)
    sb = set(b)
    if len(sa.intersection(sb)) > 0:
        print 'YES'
    else:
        print 'NO'
