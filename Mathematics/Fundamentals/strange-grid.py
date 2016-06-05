# Python 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

r,c = [int(x) for x in raw_input().split()]

if r%2 == 1:
    d = r/2
    answer = 10*d + 2*c - 2
else:
    d = (r - 1)/2
    answer = 10*d + 2*c - 1
    
print answer 