# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())

tup = ()

for x in raw_input().split():
	tup += (int(x),)
    
print hash(tup)