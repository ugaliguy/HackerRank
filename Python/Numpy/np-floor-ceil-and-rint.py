import numpy

a = map(float, raw_input().split())
a = numpy.array(a, float)

print numpy.floor(a)
print numpy.ceil(a)
print numpy.rint(a)