# Enter your code here. Read input from STDIN. Print output to STDOUT

word = sorted(raw_input())

low = list(filter(str.islower, word))
upper = list(filter(str.isupper, word))
number = list(filter(str.isdigit, word)) 
odd = list(filter(lambda x : int(x)%2 == 1, number)) 
even = list(filter(lambda x : int(x)%2 == 0, number)) 
word = low + upper + odd + even

print reduce(lambda x,y: x+y, word)