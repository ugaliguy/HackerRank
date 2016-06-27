# Python 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())
a_coord = []
b_coord = []
for i in range(n):
    a,b = [int(j) for j in raw_input().split()]
    a_coord.append(a)
    b_coord.append(b)
    
min_a = min(a_coord)
min_b = min(b_coord)

answer = min_a*min_b
print answer