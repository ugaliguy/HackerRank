# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

n = int(raw_input())

words = OrderedDict()

for i in range(n):
    word = raw_input()
    if word in words:
        words[word] += 1
    else:
        words[word] = 1
        
print len(words.keys())

for word in words:
    print words[word],