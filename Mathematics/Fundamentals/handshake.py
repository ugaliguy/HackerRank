# Python 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    handshakes = n*(n-1)/2 # Note this is nC2 i.e. n "choose" 2
    print handshakes   