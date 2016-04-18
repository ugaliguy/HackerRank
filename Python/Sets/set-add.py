# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())

countries = set()
for i in range(n):
    countries.add(raw_input())
    
print len(countries)