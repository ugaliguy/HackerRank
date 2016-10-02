# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def is_perfect_square(x):
    if x < 0:
        return False
    y = int(math.sqrt(x))
    while y*y < x:
        y += 1
    while y*y > x:
        y -= 1
    return y*y == x

t = int(raw_input())

for i in range(t):
    d,p = [int(j) for j in raw_input().split()]
    disc = d**2 + 4*p
    is_disc_square = is_perfect_square(disc)
    answer = -1
    if (d < 0) or disc < 0 or (not is_disc_square):
        answer = 0
    elif (d == 0) and (disc == 0):
        answer = 1
    elif ((d == 0) and (disc != 0)) or ((d != 0) and (disc == 0)):
        answer = 2
    elif d > 0 and disc > 0 and is_disc_square:
        answer = 4
    print answer