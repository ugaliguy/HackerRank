# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

t = int(raw_input())

for i in range(t):
    n = int(raw_input())
    sides = deque(map(int, raw_input().split()))
    
    if sides[0] > sides[-1]:
        cube = sides.popleft()
    else:
        cube = sides.pop()
        
    while(len(sides) > 0):
        if sides[0] >= sides[-1] and sides[0] <= cube:
            cube = sides.popleft()
        elif sides[0] <= sides[-1] and sides[-1] <= cube:
            cube = sides.pop()
        else:
            break
        
    if len(sides) == 0:
        print "Yes"
    else:
        print "No"