# Pthon 2

import sys


n = int(raw_input().strip())
grid = []
for t in xrange(n):
    row = str(raw_input().strip())
    grid.append(row)
for r in range(1,n-1):
    for c in range(1,n-1):
        up = grid[r][c] > grid[r-1][c]
        down = grid[r][c] > grid[r+1][c]
        left = grid[r][c] > grid[r][c-1]
        right = grid[r][c] > grid[r][c+1]
        if up and down and left and right:
            grid[r] = grid[r][0:c] + 'X' + grid[r][c+1:]
for row in range(n):
    print grid[row]