# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

word = int(raw_input())

sales = OrderedDict()

for i in range(n):
    duh = raw_input().split()
    net_price = int(duh[-1])
    item_name = ' '.join(duh[0:-1])
    if item_name in sales:
        sales[item_name] += int(net_price)
    else:
        sales[item_name] = int(net_price)
        
for item in sales:
    print item + ' ' + str(sales[item])