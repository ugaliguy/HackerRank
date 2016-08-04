# Python 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

n,m = [int(i) for i in raw_input().split()]

candies = 0
for j in range(m):
    a,b,k = [int(p) for p in raw_input().split()]
    jars = b - a + 1
    candies += jars*k
    
average = candies/n

print average