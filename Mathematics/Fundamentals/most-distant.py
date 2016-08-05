# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

n = int(raw_input())
x_coord = []
y_coord = []
for i in range(n):
    x,y = [int(j) for j in raw_input().split()]
    if (x != 0) or (x == 0 and y == 0):
        x_coord.append(x)
    elif (y != 0) or (x == 0 and y == 0):
        y_coord.append(y)
        
maxx = max(x_coord)*1.0
maxy = max(y_coord)*1.0
minx = min(x_coord)*1.0
miny = min(y_coord)*1.0

answer = max(math.sqrt(maxx**2 + maxy**2), math.sqrt(maxx**2 + miny**2), 
             math.sqrt(minx**2 + maxy**2), math.sqrt(minx**2 + miny**2), 
             abs(maxx - minx), abs(maxy - miny))

print "%.6f" % answer # This gives precision within 10^(-6)
