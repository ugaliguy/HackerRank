# Enter your code here. Read input from STDIN. Print output to STDOUT

n,k = [int(i) for i in raw_input().split()]

prob = [float(i) for i in raw_input().split()]
profit = [float(i) for i in raw_input().split()]
loss = [float(i) for i in raw_input().split()]

expect = []
for i in range(n):
    e = prob[i]*profit[i] - (1-prob[i])*loss[i]
    if e > 0:
        expect.append(round(e,2))
        
expect.sort()

value = 0
if len(expect) == 0:
    value = 0
elif len(expect) <= k:
    value = sum(expect)
else:
    for j in range(k):
        value += expect[-1-j]
        
print "%.2f" % round(value, 2)
