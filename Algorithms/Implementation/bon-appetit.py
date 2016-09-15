# Enter your code here. Read input from STDIN. Print output to STDOUT

n,k = [int(i) for i in raw_input().split()]
c = [int(i) for i in raw_input().split()]
b_charged = int(raw_input())
b_act = (sum(c) - c[k])/2
refund = b_charged - b_act

if b_charged == b_act:
    print "Bon Appetit"
else:
    print refund

