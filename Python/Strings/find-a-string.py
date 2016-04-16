# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import print_function

string = raw_input().strip()
word = raw_input().strip()

w = len(word)
count = 0

for i in range(len(string) - w + 1):
	if string[i:i + w] == word:
		count += 1

print(count)