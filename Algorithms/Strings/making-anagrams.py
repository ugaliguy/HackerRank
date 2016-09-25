# Enter your code here. Read input from STDIN. Print output to STDOUT

def letters(s):
    chars = {}
    for ch in s:
        if ch not in chars:
            chars[ch] = 1
        else:
            chars[ch] += 1
    return chars

a = raw_input().strip()
b = raw_input().strip()

a_chars = letters(a)
b_chars = letters(b)

count = 0

for key in a_chars.keys():
    if key not in b_chars.keys():
        count += a_chars[key]
    else:
        count += max(0, a_chars[key] - b_chars[key])
        
for key in b_chars.keys():
    if key not in a_chars.keys():
        count += b_chars[key]
    else:
        count += max(0, b_chars[key] - a_chars[key])
        
print count
