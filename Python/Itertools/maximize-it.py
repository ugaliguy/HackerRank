# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product, chain

k, m = list(map(int, raw_input().split())) # k is the number of lists

lists = []
prod = [0]
for i in range(k):
    list_i = list(map(int, raw_input().split()))
    list_i = list_i[1:len(list_i)]
    lists.append(list(map(int, list_i)))

prod = list(product(*lists))
mod_list = []
max = 0

for vector in prod:
    sum = 0
    for j in vector:
		sum += j**2
    if sum%m > max:
        max = sum%m
        
print max