import numpy

a = map(int, raw_input().split())
a = numpy.array(a)

b = map(int, raw_input().split())
b = numpy.array(b)

print numpy.inner(a,b)
print numpy.outer(a,b)