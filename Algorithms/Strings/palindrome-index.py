# Enter your code here. Read input from STDIN. Print output to STDOUT

def is_palindrome(s):
    rs = s[::-1]
    return s == rs

t = int(raw_input())

for case in range(t):
    s = raw_input().strip()
    if is_palindrome(s):
        print -1
    else:
        for i in range(len(s)/2):
            if s[i] != s[len(s) - i - 1]:
                if is_palindrome(s[:i]+s[i+1:]):
                    print i
                else:
                    print len(s) - i - 1
                break
                