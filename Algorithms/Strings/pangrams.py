# Enter your code here. Read input from STDIN. Print output to STDOUT

s = raw_input().strip()
chars = set()
for ch in s:
    chars.update(ch.upper())

if len(chars) == 27:
    print 'pangram'
else:
    print 'not pangram'