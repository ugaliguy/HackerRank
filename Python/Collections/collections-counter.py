# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

shoes = int(raw_input())
sizes = list(map(int, raw_input().split()))
inventory = Counter(sizes)
customers = int(raw_input())

earnings = 0
for i in range(customers):
	size, price = list(map(int, raw_input().split()))
	if size in inventory.keys():
		if inventory[size] > 0:
			earnings += price
			inventory[size] -= 1

print earnings