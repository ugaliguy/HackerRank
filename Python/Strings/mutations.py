# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import print_function

chars = list(raw_input())
arr = raw_input().split()

chars[int(arr[0])] = arr[1]
result = "".join(chars)
print(result)