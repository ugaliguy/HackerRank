import re


Regex_Pattern = r"\w{3}\W\w{10}\W\w{3}"	# Do not delete 'r'.
print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())