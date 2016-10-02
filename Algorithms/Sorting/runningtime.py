# Enter your code here. Read input from STDIN. Print output to STDOUT

def insertion_sort(l):
    shift = 0
    for i in xrange(1, len(l)):
        j = i-1 
        key = l[i]
        while (j >= 0) and (l[j] > key):
            l[j+1] = l[j]
            shift += 1
            j -= 1
        l[j+1] = key
    print shift

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertion_sort(ar)
