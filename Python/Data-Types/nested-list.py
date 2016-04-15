# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import print_function

n = int(raw_input())
records = []
scores = []

for i in range(n):
    name = raw_input()
    score = raw_input()
    scores.append(float(score)) 
    records.append([name, float(score)])
    
min_score = min(scores)
indices = []
second_scores = []
for i in range(n):
    if scores[i] > min_score:
        indices.append(i)
        second_scores.append(scores[i])
        
second = min(second_scores)

result = []
for j in indices:
    if records[j][1] == second:
        result.append(records[j][0])
        
result = sorted(result)

print(*result, sep="\n")