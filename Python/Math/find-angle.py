# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

ab = int(raw_input())
bc = int(raw_input())

ac = math.sqrt(ab**2 + bc**2)
alpha = math.asin(ab/ac)

mc = 0.5*ac
bm = math.sqrt(bc**2 + mc**2 - 2*bc*mc*math.cos(alpha))

theta = math.degrees(math.asin(math.sin(alpha)*mc/bm))

theta = str(int(round(theta)))

print(theta + "°")