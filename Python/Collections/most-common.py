# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

word = sorted(Counter(raw_input()).items(), key= lambda x: (-x[1],x[0]))[:3]
print("\n".join(x[0]+" "+str(x[1]) for x in word))

# The code below passed all but one test.
# I'm still trying to figure out how it failed.

# freq = Counter(word).most_common(3)

# for pair in freq:
#     print pair[0], pair[1]

