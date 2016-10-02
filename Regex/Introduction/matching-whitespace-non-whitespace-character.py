import re


Regex_Pattern = r"\S{2}\s\S{2}\s\S{2}"	# Do not delete 'r'.
print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())