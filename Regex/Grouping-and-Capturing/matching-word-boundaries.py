import re


Regex_Pattern = r'\b[aeiouAEIOU][A-Za-z]*\b'	# Do not delete 'r'.
print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())