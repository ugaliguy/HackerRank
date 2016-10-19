#!/bin/python

import sys

def make_change(coins, n):
    coins = sorted(coins)
    ways = {}
    for i in range(n+1):
        ways[i] = 0
    for i in range(0, n+1, coins[0]):
        ways[i] = 1
    for coin in coins[1:]:
        for amount in range(coin, n+1):
            # If there's a way for the previous coin to make change
            if ways[amount-coin] != 0: 
                ways[amount] += ways[amount - coin]
    return ways[n]

n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
coins = map(int,raw_input().strip().split(' '))
print make_change(coins, n)
