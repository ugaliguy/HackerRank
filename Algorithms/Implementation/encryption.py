# Python 2

import sys
import math


s = raw_input().replace(" ", "")
sq = math.sqrt(len(s))
col = int(math.ceil(sq))

for j in range(col):
    print s[j::col],