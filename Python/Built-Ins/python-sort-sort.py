# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = map(int, raw_input().split())
rows = []
for i in range(n):
    rows.append(map(int, raw_input().split()))

k = int(raw_input())
rows = sorted(rows, key=lambda x: x[k])

for row in rows:
    for j in range(m):
        if j < m-1:
            print row[j],
        else:
            print row[m-1]