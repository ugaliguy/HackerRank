# Python 2

p = int(raw_input())
q = int(raw_input())
kap = []
for n in range(p,q+1):
    sq = list(str(n**2))
    length = len(sq)
    l = 0
    r = 0
    left = ''.join(sq[:length/2])
    if left != '':
        l = int(left)
    else:
        l = 0
    right = ''.join(sq[length/2:])
    if right != '':
        r = int(right)
    else:
        r = 0
        
    if n == l+r:
        kap.append(n)
        
if len(kap) > 0:
    for i in kap:
        print i,
else:
    print "INVALID RANGE"