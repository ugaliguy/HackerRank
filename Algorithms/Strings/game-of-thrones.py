def letters(s):
    chars = {}
    for ch in list(s):
        if ch not in chars:
            chars[ch] = 1
        else:
            chars[ch] += 1
    return chars
            
s = raw_input()
 
# Write the code to find the required palindrome and then assign the variable 'found' a value of True or False
letters = letters(s)
ones = 0
for key in letters.keys():
    if letters[key]%2 == 1:
        ones += 1
        
if ones > 1:
    print("NO")
else:
    print("YES")
