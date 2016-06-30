# Python 2

# See the following post from StackOverflow for an explanation
# http://stackoverflow.com/questions/24244432/collision-detection-between-
# two-accelerating-spheres-with-no-initial-velocity


# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def mag(p):
    dim = len(p)
    total = 0
    for i in range(dim):
        total += p[i]**2
    mag = math.sqrt(total)
    return mag

def dist(p,q):
    dim = len(p)
    diff = [p[i]-q[i] for i in range(dim)]
    return mag(diff)

def add(p,q):
    dim = len(p)
    add = [p[i]+q[i] for i in range(dim)]
    return add

def diff(p,q):
    dim = len(p)
    diff = [p[i]-q[i] for i in range(dim)]
    return diff 

def scalar(p,c):
    dim = len(p)
    scalar = [p[i]*c for i in range(dim)]
    return scalar

def dot(p,q):
    dim = len(p)
    dots = [p[i]*q[i] for i in range(dim)]
    return sum(dots)
    
t = int(raw_input())

for i in range(t):
    r1,r2 = [int(j) for j in raw_input().split()]
    p1 = [int(j) for j in raw_input().split()]
    a1 = [int(j) for j in raw_input().split()]
    p2 = [int(j) for j in raw_input().split()]
    a2 = [int(j) for j in raw_input().split()]
    p = diff(p1,p2)
    a = diff(a1,a2)
    time = max(-1.0*dot(a,p)/dot(a,a),0.0)
    radii = r1 + r2
    post = add(p,scalar(a,time)) # 'post' is 'position at time t'
    check = dot(post,post)
    if check <= radii**2:
        print 'YES'
    else:
        print 'NO'
  