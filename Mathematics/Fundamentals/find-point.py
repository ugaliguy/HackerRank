# Python 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(raw_input())
for i in range(t):
    px,py,qx,qy = raw_input().split()
    sx = 2*int(qx) - int(px)
    sy = 2*int(qy) - int(py)
    print str(sx) + ' ' + str(sy)