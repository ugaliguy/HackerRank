# Enter your code here. Read input from STDIN. Print output to STDOUT
size = int(raw_input()) #The size of each group
guests = list(map(int, raw_input().split()))
rooms = set(guests) # The set of distinct room numbers

room = (sum(rooms)*size - sum(guests))/(size - 1)

print room