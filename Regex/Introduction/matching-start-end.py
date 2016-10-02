import re


Regex_Pattern = r"^\d\w{4}\.$"	# Do not delete 'r'.
print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())