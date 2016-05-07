import numpy

n, m, p = map(int, raw_input().split())
entries_1 = []
entries_2 = []

for i in range(n):
	entries_1.append(map(int, raw_input().split()))

matrix_1 = numpy.array(entries_1)
matrix_1 = numpy.reshape(matrix_1, (n,p))

for j in range(m):
	entries_2.append(map(int, raw_input().split()))

matrix_2 = numpy.array(entries_2)
matrix_2 = numpy.reshape(matrix_2, (m,p))

print numpy.concatenate((matrix_1,matrix_2), axis = 0)