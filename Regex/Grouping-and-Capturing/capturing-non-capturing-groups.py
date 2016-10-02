import re


Regex_Pattern = r'(ok){3,}'	# Do not delete 'r'.
print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())