n = int(raw_input().strip())
a = [int(i) for i in raw_input().strip().split(' ')]

total = 0
swaps = -1

while(swaps != 0):
    swaps = 0
    for i in xrange(n-1):
        if a[i] > a[i+1]:
            swaps += 1
            a[i], a[i+1] = a[i+1], a[i]
    
    total += swaps

print"Array is sorted in %d swaps." % (total)
print "First Element: %s" % a[0]
print "Last Element: %s" % a[n-1]