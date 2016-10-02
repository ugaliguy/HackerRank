# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())

daily_max = []
for i in range(n):
    x,y,z = [int(j) for j in raw_input().split()]
    m = max(x+y, x+z, y+z)
    daily_max.append(m)
    
print max(daily_max)
  