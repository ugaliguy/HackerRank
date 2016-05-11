import numpy

n = int(raw_input())
a = []
for i in range(n):
	a += map(float, raw_input().split())

a = numpy.array(a)
a = numpy.reshape(a, (n,n))

print numpy.linalg.det(a)