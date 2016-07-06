# Python 3

# Enter your code here. Read input from STDIN. Print output to STDOUT

def orientation(ax,ay,bx,by,cx,cy): # Check if three points have an orientation or are co-linear
    value = (by-ay)*(cx-bx) - (bx-ax)*(cy-by)
    if value == 0:
        return 0 # The points are co-linear
    elif value > 0:
        return 1 # The points have clockwise orientation
    else:
        return -1 # The points have counterclockwise orientation

def on_segment(ax,ay,bx,by,cx,cy): # Check if point c is on segment from a to b
    return (cx <= max(ax,bx) and cx >= min(ax,bx)) and (cy <= max(ay,by) and cy >= min(ay,by))

def intersect(ax,ay,bx,by,cx,cy,dx,dy):
    or1 = orientation(ax,ay,bx,by,cx,cy)
    or2 = orientation(ax,ay,bx,by,dx,dy)
    or3 = orientation(cx,cy,dx,dy,ax,ay)
    or4 = orientation(cx,cy,dx,dy,bx,by)
    if (or1 != or2 and or3 != or4):
        return True
    if or1 == 0 and on_segment(ax,ay,cx,cy,bx,by):
        return True
    if or2 == 0 and on_segment(ax,ay,dx,dy,bx,by):
        return True
    if or3 == 0 and on_segment(cx,cy,ax,ay,dx,dy):
        return True
    if or4 == 0 and on_segment(cx,cy,bx,by,dx,dy):
        return True
    
    return False

t = int(raw_input())

for i in range(t):
    x1,y1,x2,y2,xm,ym = [int(j) for j in raw_input().split()]
    # I'm not sure why we needed to check both line segments in the following:
    if intersect(x1,y1,x2,y2,xm,ym,0,0) and intersect(x1,y1,x2,y2,0,0,xm,ym):
        print 'NO'
    else:
        print 'YES'