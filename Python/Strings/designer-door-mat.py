N, M = map(int,raw_input().split()) # More than 6 lines of code will result in 0 score. 
for i in range(1,N,2): 			# Blank lines are not counted.
    print (".|."*i).center(M,'-')
print "WELCOME".center(M,'-')
for i in range(N-2,-1,-2): 
    print (".|."*i).center(M,'-')