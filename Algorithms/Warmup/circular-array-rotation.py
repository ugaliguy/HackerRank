# Enter your code here. Read input from STDIN. Print output to STDOUT

n,k,q = [int(i) for i in raw_input().split()]
arr = [int(j) for j in raw_input().split()]

# Note rotating n times brings us back to the original array
# so reduce k modulo n
k = k%n 
arr = arr[-k:] + arr[:-k] # [last k items] + [everything except last k items]

for i in range(q):
    m = int(raw_input())
    print arr[m]
      