# Enter your code here. Read input from STDIN. Print output to STDOUT

sizes = raw_input().split()
m = int(sizes[0])
n = int(sizes[1])
input_array = raw_input().split()
array = list(input_array)
array = [int(a) for a in array]

input_A = raw_input().split()
A = set([int(a) for a in input_A])

input_B = raw_input().split()
B = set([int(a) for a in input_B])

happiness = 0
for i in array:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1
        
print happiness