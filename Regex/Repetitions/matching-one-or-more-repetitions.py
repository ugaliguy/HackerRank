import re


Regex_Pattern = r'^\d+[A-Z]+[a-z]+$'	# Do not delete 'r'. 
print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())