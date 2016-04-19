A = set(raw_input().split())
b = int(raw_input());

product = 1
for i in range(b):
    B = set(raw_input().split())
    if (A.issuperset(B) and (len(A) > len(B))):
        product *= 1
    else:
        product *= 0
        
if product == 1:
    print True
else:
    print False