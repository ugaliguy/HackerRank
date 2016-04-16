# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())
alpha = 'abcdefghijklmnopqrstuvwxyz'
length = 4*n - 3

for i in range(n):
    if i > 0:
        print(('-'.join(alpha[n-1:n-i-1:-1]) + '-' + '-'.join(alpha[n-i-1:n])).center(length,'-'))
    else:
        print(alpha[n-1].center(length,'-'))
    
for j in range(1,n):
    print(('-'.join(alpha[n-1:j-1:-1]) + '-' + '-'.join(alpha[j+1:n])).center(length,'-'))