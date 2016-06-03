# Python 2

# Jim is off to a party and is searching for a matching pair of socks. 
# His drawer is filled with socks, each pair of a different color. 
# In its worst case scenario, how many socks (x) should Jim remove from his drawer 
# until he finds a matching pair?

# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(raw_input())
for i in range(t):
	n = int(raw_input())
	d = n + 1 # Use the Pigeon Hole Principle
	print str(d)