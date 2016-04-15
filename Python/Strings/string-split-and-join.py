# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import print_function

input_string = raw_input()
split_string = input_string.split(" ")
join_string = "-".join(split_string)

print(join_string)