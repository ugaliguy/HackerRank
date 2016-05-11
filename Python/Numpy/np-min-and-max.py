import numpy

n, m = map(int, raw_input().split())

a = []
for i in range(n):
	a += map(int, raw_input().split())

a = numpy.array(a)
a = numpy.reshape(a, (n,m))

a_min = numpy.min(a, axis = 1)

print numpy.max(a_min)