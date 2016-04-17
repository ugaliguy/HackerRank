# Enter your code here. Read input from STDIN. Print output to STDOUT

string = raw_input()
vowels = 'AEIOU'

stuart = 0 # Keep track of consonants
kevin = 0 # Keep track of vowels

# NOTE - using len(string[i:]) is more costly than using len(string) - i
for i in range(len(string)):
    if string[i] in vowels:
        kevin += len(string)-i
    else:
        stuart += len(string)-i
        
if stuart > kevin:
    print("Stuart " + str(stuart))
elif stuart < kevin:
    print("Kevin " + str(kevin))
else:
    print("Draw")	