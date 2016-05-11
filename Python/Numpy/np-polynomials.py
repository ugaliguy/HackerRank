import numpy

a = list(map(float, raw_input().split()))
val = float(raw_input())

print numpy.polyval(a, val)