# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input()) # Cardinality of the set a
a = set(map(int, raw_input().split())) # The set a

k = int(raw_input()) # The number of other sets

for i in range(k):
    (command, other_set_card) = raw_input().split()
    other_set = set(map(int, raw_input().split()))

    if command == "update":
        a.update(other_set)
    elif command == "intersection_update":
        a.intersection_update(other_set)
    elif command == "difference_update":
        a.difference_update(other_set)
    elif command == "symmetric_difference_update":
        a.symmetric_difference_update(other_set)
    
print(sum(a))