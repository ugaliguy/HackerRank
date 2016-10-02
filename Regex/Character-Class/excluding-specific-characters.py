import re


Regex_Pattern = r'^[^\d][^aeiou][^bcDF][^\r\n\t\f\s][^AEIOU][^\.,]$'	# Do not delete 'r'.
print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())