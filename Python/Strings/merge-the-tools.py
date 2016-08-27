# Enter your code here. Read input from STDIN. Print output to STDOUT
import sets

s = raw_input()
n = len(s)
k = int(raw_input())

sub = []
for i in range(n/k):
    sub.append(s[k*i:k*(i+1)])

for word in sub:
    wordset = sets.Set(word)
    if len(word) == len(wordset):
        print word
    else:
        answer = ''
        for j in range(0,len(word)):
            if word[j] in wordset:
                answer += word[j]
                wordset.discard(word[j])
        print answer
            