# Python 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

n,k = [int(i) for i in raw_input().split()]
probs = [int(j) for j in raw_input().split()]
special = 0 # number of special problems
pages = []
for ch in probs:
    if ch%k == 0:
        pages.append(ch/k)
    else:
        pages.append((ch/k)+1)
# print pages
for chap in range(n):
    for page in range(pages[chap]):
        current = sum(pages[:chap])+page + 1
        first = k*page + 1
        last = min(first + k - 1, probs[chap])
        # print 'current = ' + str(current)
        # print 'first = ' + str(first)
        if (first <= current) and (current <= last):
            special += 1
        
print special