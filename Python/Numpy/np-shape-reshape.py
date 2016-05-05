import numpy

entries = list(map(int, raw_input().split()))
initial = numpy.array(entries)

three_by_three = numpy.reshape(initial, (3,3))

print three_by_three