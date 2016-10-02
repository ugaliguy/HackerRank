# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(raw_input())

for i in range(t):
    MOD = 10**9 + 7
    s = int(input())
    k = s/20
    rem = s%20
    if rem == 0:
        print (42*k - 2)%MOD
    else:
        print (42*k + 2*rem)%MOD

	# The following code times out on the tests
	# but I think it works
	# 
    # s = int(raw_input())%(10**9 + 7)
    # # k = s/20
    # # square = 2*s + k
    # square = 0
    # while s != 0:
    #     square += 1
    #     if square%2 == 0 and square%42 != 0:
    #         s -= 1
        
    #     print "square = " + str(square) + " s = " + str(s)
    # print square
