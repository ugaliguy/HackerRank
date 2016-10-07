# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())
sticks = [int(i) for i in raw_input().split()]
sticks.sort()

i = n-3
while i >= 0 and (sticks[i] + sticks[i+1] <= sticks[i+2]) :
    i -= 1

if i >= 0 :
    print str(sticks[i]) + ' ' + str(sticks[i+1]) + ' ' + str(sticks[i+2])
else :
    print -1