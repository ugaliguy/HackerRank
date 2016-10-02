# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input().strip())
box = []
for i in range(n):
    s = set(raw_input().strip())
    box.append(s)
    
common = box[0]
for j in range(1,len(box)):
    common = common.intersection(box[j])
    
print len(common)
