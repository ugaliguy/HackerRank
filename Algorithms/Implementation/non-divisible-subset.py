# Enter your code here. Read input from STDIN. Print output to STDOUT

n,k = [int(i) for i in raw_input().split()]

numbers = [int(i) for i in raw_input().split()]


# This code has a bug in it - Fix it!

mod_k = {j:[] for j in range(k)}

for i in range(n):
    mod_k[numbers[i]%k].append(numbers[i])

count = 0
if len(mod_k[0]) > 1:
    count = 1
    
pairs = set([(j,k-j) for j in range(1,k/2+1)])  
for p,q in pairs:
    if p != q:
        if len(mod_k[p]) > len(mod_k[q]):
            count += len(mod_k[p])
        else:
            count += len(mod_k[q])
    else:
        if len(mod_k[p]) > 0:
            count += 1
print count