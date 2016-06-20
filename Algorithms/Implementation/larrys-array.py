# Python 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

def inversions(arr):
    if len(arr) == 1:
        return 0
    else:
        inv = len(arr) - arr.index(max(arr)) - 1
        arr.remove(max(arr))
        return inv + inversions(arr)

t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    a = [int(j) for j in raw_input().split()]
    if inversions(a)%2 == 0:
        print 'YES'
    else:
        print 'NO'