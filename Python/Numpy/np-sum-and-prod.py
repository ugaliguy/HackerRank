import numpy

n, m = map(int, raw_input().split())

a = []
for i in range(n):
    a.append(list(map(int, raw_input().split())))
    
a = numpy.array(a)
a = numpy.reshape(a, (n,m))

a_sum = numpy.sum(a, axis = 0)
result = numpy.product(a_sum)

print result