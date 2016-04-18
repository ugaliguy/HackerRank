# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import print_function

string = raw_input().strip()
chars = list(string)

alpha = []
digit = []
lower = []
upper = []
for char in chars:
	if char.isalpha():
		alpha.append(char)

	if char.isdigit():
		digit.append(char)

	if char.islower():
		lower.append(char)

	if char.isupper():
		upper.append(char)		

print(char.isalnum())
print(len(alpha) > 0)
print(len(digit) > 0)
print(len(lower) > 0)
print(len(upper) > 0)
