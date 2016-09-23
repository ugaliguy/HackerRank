# Enter your code here. Read input from STDIN. Print output to STDOUT

def letters(s):
    chars = {}
    for ch in s:
        if ch not in chars:
            chars[ch] = 1
        else:
            chars[ch] += 1
    return chars
            
t = int(raw_input())

for case in range(t):
    s = raw_input().strip()
    length = len(s)
    count = 0
    if length%2 == 1:
        print -1
    else:
        s1 = s[0:length/2]
        s2 = s[length/2:length]
        s1_chars = letters(s1)
        s2_chars = letters(s2)
        
        for key in s1_chars.keys():
            if key not in s2_chars:
                count += s1_chars[key]
            else:
                count += max(0, s1_chars[key] - s2_chars[key])
        print count