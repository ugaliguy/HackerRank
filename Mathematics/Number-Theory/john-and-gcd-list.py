# Enter your code here. Read input from STDIN. Print output to STDOUT

def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)
    
def lcm(a,b):
    return a*b/gcd(a,b)

t = int(raw_input())

for i in range(t):
    n = int(raw_input())
    a_list = [int(j) for j in raw_input().split()]
    b_list = [a_list[0]]
        
    for j in range(1,n):
        b_list.append(lcm(a_list[j-1],a_list[j]))
    b_list.append(a_list[-1]) 
    for b in b_list[0:n]:
        print b,
    print b_list[n]
            