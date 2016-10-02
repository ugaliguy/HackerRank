# Enter your code here. Read input from STDIN. Print output to STDOUT

def reduce(word, i):
    return word[0:i]+word[i+2:len(word)]

s = raw_input().strip()

i=0
while (i<len(s)):
    if(s[i:i+1] == s[i+1:i+2]):
        s = reduce(s,i)
        i = 0
    else:
        i = i + 1
    
if s=='':
    print "Empty String"
else:
    print s
        