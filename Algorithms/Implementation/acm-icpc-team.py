# Python 2

import sys


n,m = [int(i) for i in raw_input().split()]

people = []
count_topics = 0
count_teams = 0

for j in range(n):
    top = str(raw_input().strip())
    people.append(top)
    
for p in range(n):
    for q in range(p+1,n):
        bin1 = int(people[p],2)
        bin2 = int(people[q],2)
        topics = bin(bin1 | bin2).count('1')

        if topics > count_topics:
            count_topics = topics
            count_teams = 1
        elif topics == count_topics:
            count_teams += 1
            
print count_topics
print count_teams 