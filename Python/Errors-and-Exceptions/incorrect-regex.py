# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

t = int(raw_input())

for i in range(t):
    try:
        x = re.compile(raw_input())
        if x:
            print True
    except:
        print False