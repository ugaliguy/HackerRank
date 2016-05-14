# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())

fib = lambda y: y if y < 2 else fib(y - 1) + fib(y - 2) # Calculates nth Fibonacci number from 0th Fibonacci number
fibs = lambda n: map(fib, range(n))

cube = lambda a: a**3

result = map(cube, fibs(n))

print result