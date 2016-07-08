# Python 2

#!/bin/python

import sys


n1,n2,n3  = [int(i) for i in raw_input().split()]
h1 = map(int,raw_input().strip().split(' '))
h2 = map(int,raw_input().strip().split(' '))
h3 = map(int,raw_input().strip().split(' '))

piles = [h1, h2, h3]
heights = [sum(j) for j in piles]

for cylinder in range(n1+n2+n3):
    min_height = min(heights)
    max_height = max(heights)
    max_index = heights.index(max_height)
    tallest = piles[max_index]
    while min_height < max_height:
        trim = tallest[0]
        tallest.pop(0)
        max_height -= trim
    heights[max_index] = max_height
    if heights[0] == heights[1] and heights[0] == heights[2]:
        break
print heights[0]