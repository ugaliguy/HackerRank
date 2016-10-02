import re

Test_String = raw_input()

Regex_Pattern = r'hackerrank'	# Do not delete 'r'.
match = re.findall(Regex_Pattern, Test_String)

print "Number of matches :", len(match)