# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

string = raw_input()

for key, value in groupby(string):
    print (len(list(value)), int(key)),