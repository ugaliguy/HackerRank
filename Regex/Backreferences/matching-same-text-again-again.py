import re


Regex_Pattern = r'([a-z])(\w)(\s)(\W)(\d)(\D)([A-Z])([A-Za-z])([aeiouAEIOU])(\S)\1\2\3\4\5\6\7\8\9\10'	# Do not delete 'r'.
print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())