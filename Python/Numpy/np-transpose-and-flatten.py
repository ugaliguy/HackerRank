import numpy

n, m = map(int, raw_input().split())
entries = []

for i in range(n):
	entries.append(map(int, raw_input().split()))

initial = numpy.array(entries)
n_by_m = numpy.reshape(initial, (n,m))

print numpy.transpose(n_by_m)

print n_by_m.flatten() # Note this does not flatten the transpose