# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

n = int(raw_input())
d = deque()

for i in range(n):
    duh = list(raw_input().split())
    method = duh[0]
    if len(duh) == 2:
        val = duh[1]
        if method == 'append':
            d.append(val)
        elif method == 'appendleft':
            d.appendleft(val)
    else:
        if method == 'pop':
            d.pop()
        elif method == 'popleft':
            d.popleft()
            
for item in d:
    print item,