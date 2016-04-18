# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(raw_input())

input_plants = raw_input()
plants = input_plants.split()
distinct_plants = set(plants)
total = 0

for p in distinct_plants:
    total += int(p)
    
avg = (total + 0.0)/len(distinct_plants)

print(avg)