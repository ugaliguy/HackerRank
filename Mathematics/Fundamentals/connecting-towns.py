# Python 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    towns = raw_input().split()
    towns = [int(i) for i in towns] # This is a list comprehension
    answer = 1
    for i in towns:
        answer *= i
    answer = answer%1234567 # This modulus is only to prevent overflow
    						# from extremely large integers
    print answer