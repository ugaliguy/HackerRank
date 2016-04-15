# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())
arr = raw_input()
numb = arr.split()
numbers = list(map(int, numb))

max_1 = max(numbers)
numbers_2 = [numbers[i] for i in range(len(numbers)) 
			 if numbers[i] != max_1]
max_2 = max(numbers_2)

print(max_2)