import re


Regex_Pattern = r'^\d{2,}[a-z]*[A-Z]*$'	# Do not delete 'r'.
print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())