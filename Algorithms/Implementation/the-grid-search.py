# Python 2

import sys

def search_inside(G, P, R, C, r, c):
    for i in range(R - r + 1):
        for j in range(C - c + 1):
            valid = True
            for k in range(r):
                if G[i + k][j:j + c] != P[k]:
                    valid = False
                    break

            if valid:
                print 'YES'
                return

    print 'NO'

t = int(raw_input())
for i in range(t):
    R,C = [int(j) for j in raw_input().split()]
    
    G = []
    for g in range(R):
       G_m = str(raw_input().strip())
       G.append(G_m)

    r,c = [int(k) for k in raw_input().split()]
    P = []
    for p in range(r):
       P_n = str(raw_input().strip())
       P.append(P_n)
    search_inside(G, P, R, C, r, c)