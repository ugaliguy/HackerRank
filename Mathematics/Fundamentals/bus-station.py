# Python 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())
groups = [int(i) for i in raw_input().split()]
sums = []
partial = 0
for group in groups:
    partial += group
    sums.append(partial)
sums_set = set(sums)
total = max(sums)

answer = []
seats = set()
min_seats = max(groups)
for s in sums:
    if s < min_seats:
        continue
    m = 1
    while(True):
        mult = s*m
        if mult == total:
            seats.add(s)
            break
        elif mult > total:
            break
        elif mult not in sums_set:
            break
        else:
            m += 1
            
seats = sorted(seats)        
for k in list(seats):
    print str(k),