# Python 2

# This is a lousy problem. Anyone who knows some linear algebra should be offended.
# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(raw_input())

for i in range(t):
    x1,y1,z1 = [int(j) for j in raw_input().split()]
    x2,y2,z2 = [int(j) for j in raw_input().split()]
    x3,y3,z3 = [int(j) for j in raw_input().split()]
    x4,y4,z4 = [int(j) for j in raw_input().split()]
    bool_x = (x1 == x2  and  x2 == x3  and  x3 == x4)
    bool_y = (y1 == y2  and  y2 == y3  and  y3 == y4)
    bool_z = (z1 == z2  and  z2 == z3  and  z3 == z4)
    if bool_x or bool_y or bool_z:
        print 'YES'
    else:
        print 'NO'