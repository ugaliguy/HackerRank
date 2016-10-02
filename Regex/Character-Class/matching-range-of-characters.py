import re

Regex_Pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z]'	# Do not delete 'r'.
print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())