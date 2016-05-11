import numpy

n = int(raw_input())

a = []
for i in range(n):
    a += map(int, raw_input().split())
a = numpy.array(a)
a = numpy.reshape(a, (n,n))

b = []
for i in range(n):
    b += map(int, raw_input().split())
b = numpy.array(b)
b = numpy.reshape(b, (n,n))

prod = numpy.dot(a,b)
print prod