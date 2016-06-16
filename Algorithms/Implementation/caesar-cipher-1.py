# Python 2

import sys


n = int(raw_input())
s = raw_input().strip()
k = int(raw_input())

key = 'abcdefghijklmnopqrstuvwxyz'
crypt = ''
for ch in s:
    if ch.isalpha():
        if ch.isupper():
            i = (key.index(ch.lower()) + k)%26
            crypt += key[i].upper()
        else:
            i = (key.index(ch) + k)%26
            crypt += key[i]
    else:
        crypt += ch
print crypt 