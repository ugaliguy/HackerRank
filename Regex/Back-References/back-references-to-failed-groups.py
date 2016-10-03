import re


Regex_Pattern = r"^(\d{2})(-?)\d{2}\2\d{2}\2\d{2}$"	# Do not delete 'r'.
print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())