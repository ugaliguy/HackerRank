import numpy

n, m = map(int, raw_input().split())

A = []
B = []

for i in range(n):
	A += map(int, raw_input().split())
A =  numpy.array(A)
A_n_m = numpy.reshape(A,(n,m))

for i in range(n):
	B += map(int, raw_input().split())
B =  numpy.array(B)
B_n_m = numpy.reshape(B,(n,m))

print A_n_m + B_n_m
print A_n_m - B_n_m
print A_n_m * B_n_m
print A_n_m / B_n_m
print A_n_m % B_n_m
print A_n_m ** B_n_m