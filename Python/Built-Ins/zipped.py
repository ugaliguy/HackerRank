# Enter your code here. Read input from STDIN. Print output to STDOUT

n, x = map(int, raw_input().split())
scores = []
for i in range(x):
    scores.append(map(float, raw_input().split()))
    
total = map(sum, zip(*scores)) 

for student in total:
    print str(student/x)