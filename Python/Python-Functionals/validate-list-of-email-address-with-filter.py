# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(raw_input())

emails = []
for i in range(n):
    emails += [raw_input()]
    
print sorted(list(filter(lambda x: 
	re.search('^[\\w-]+@[a-zA-Z\\d]+\\.[a-zA-Z\\d]{1,3}$',x), emails)))