# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(raw_input())

for i in range(t):
    s = int(raw_input())%(10**9 + 7)
    square = 0 
    while s != 0:
        square += 1
        if (square%4 == 0 or square%2 == 0) and square%42 != 0:
            s -= 1
        
        print "square = " + str(square) + " s = " + str(s)
    print square