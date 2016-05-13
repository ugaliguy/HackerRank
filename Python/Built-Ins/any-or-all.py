# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())
a = map(str, raw_input().split())

print all([int(i) > 0 for i in a]) and any([j == j[::-1] for j in a])