import re


Regex_Pattern = r'^\d{1,2}[A-Za-z]{3,}[\.]{0,3}$'	# Do not delete 'r'.
print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())