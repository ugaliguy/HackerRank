# Enter your code here. Read input from STDIN. Print output to STDOUT

def swap(arr,x,y):
    mem = arr[x]
    arr[x] = arr[y]
    arr[y] = mem
    return arr

def quick_sort_in_place(ar,start,end):
    if end-start <= 0:
        return ar
    p = ar[end]
    indx = start
    for i in xrange(start,end):
        if ar[i] <= p:
            ar = swap(ar,i,indx)
            indx += 1
        else:
            pass
    swap(ar,indx,end)
    print ' '.join(str(x) for x in ar)
    # left side
    ar = quick_sort_in_place(ar,start,indx-1)
    # right side
    ar = quick_sort_in_place(ar,indx+1,end)
    return ar

n = int(raw_input())
ar = [int(i) for i in raw_input().split()]
quick_sort_in_place(ar, 0, len(ar) - 1)