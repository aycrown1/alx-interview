#!/usr/bin/python3
"""
This module defines a Minimum Operations for a ALX interview project
"""


def minOperations(n):
    """
     A method that calculates the fewest number of operations
     needed to result in exactly n H characters in the file.
    """
    if not isinstance(n, int):
        return 0
    if n <= 1:
        return 0

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i + minOperations(n // i)

    return n
