#!/usr/bin/python3
"""
Interview question about determining the fewest number of coins needed
    to meet a given amount total
"""


def makeChange(coins, total):
    """
    Function that determine fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0
    change = [float('inf')] * (total + 1)
    change[0] = 0
    for coin in coins:
        for i in range(coin, total + 1):
            change[i] = min(change[i], change[i - coin] + 1)

    return change[total] if change[total] != float('inf') else -1
