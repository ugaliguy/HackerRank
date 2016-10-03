import re


Regex_Pattern = r'^(Mr\.|Mrs\.|Ms\.|Dr\.|Er\.)[A-Za-z]+$'	# Do not delete 'r'.
print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())