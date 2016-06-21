# Python 2

# Enter your code here. Read input from STDIN. Print output to STDOUT


def rotate_matrix(matrix, r):
    shift = 0
    while n - shift > n / 2 and m - shift > m / 2:
        top = [(shift, i) for i in range(shift, n - shift, 1)]
        right = [(i, n - 1 - shift) for i in range(shift + 1, m - 1 - shift, 1)]
        bot = [(m - 1 - shift, i) for i in range(n - 1 - shift, shift - 1, -1)]
        left = [(i, shift) for i in range(m - shift - 2,shift, -1)]
        layer = top + right + bot + left

        circle = [matrix[p[0]][p[1]] for p in layer]
        r_mod = r % len(circle)
        circle = circle[r_mod:] + circle[0:r_mod]

        for q in range(len(layer)):
            index = layer[q]
            matrix[index[0]][index[1]] = circle[q]
        shift += 1

    return matrix

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print element,
        print

        
m,n,r = [int(i) for i in raw_input().split()]
matrix = []

for j in range(m):
    matrix.append([int(k) for k in raw_input().split()])
    
rotate_matrix(matrix, r)
print_matrix(matrix)
    