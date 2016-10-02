import re


Regex_Pattern = r'^[A-Za-z]*s$'	# Do not delete 'r'. 
print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())