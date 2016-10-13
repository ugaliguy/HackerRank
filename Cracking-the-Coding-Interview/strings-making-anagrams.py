def number_needed(a, b):
 
    count = [abs(a.count(i) - b.count(i)) for i in 'abcdefghijklmnopqrstuvwxyz']

    return sum(count)
    

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
