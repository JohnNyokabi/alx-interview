#!/usr/bin/python3
"""
function that determines the fewest number of coins
needed to meet a given amount total
"""


def makeChange(coins, total):
    """method that determines the fewest numberof coins needed.
    """
    if total < 1:
        return 0
    coins.sort()
    coins.reverse()
    fewest = 0
    for coin in coins:
        if total <= 0:
            break
        buff = total // coin
        fewest += buff
        total -= (buff * coin)
    if total != 0:
        return -1
    return fewest
