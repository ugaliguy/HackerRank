import re


Regex_Pattern = r"\d{2}\D\d{2}\D\d{4}"	# Do not delete 'r'.matching-whitespace-non-whitespace-character
print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())