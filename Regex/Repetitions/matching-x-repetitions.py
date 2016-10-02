import re


Regex_Pattern = r'^[A-Za-z02468]{40}[13579\s]{5}$'	# Do not delete 'r'.
print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())