# Enter your code here. Read input from STDIN. Print output to STDOUT

string = raw_input()
words = string.split(' ')
cap_words = []

for word in words:
	cap_words.append(word.capitalize())

cap_string = ' '.join(cap_words)

print(cap_string)