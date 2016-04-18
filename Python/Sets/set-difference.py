# Enter your code here. Read input from STDIN. Print output to STDOUT

english = int(raw_input())
e = set(raw_input().split())

french = int(raw_input())
f = set(raw_input().split())

diff = e.difference(f)

print len(diff)