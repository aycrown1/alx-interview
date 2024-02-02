#!/usr/bin/python3
"""
This module is an interview challenge in python
"""


def canUnlockAll(boxes):
    """
    canUnlockAll function determines if all the boxes can be opened
    """
    keys = set([0])
    for current_key in keys.copy():
        if 0 <= current_key < len(boxes):
            keys.update(boxes[current_key])

    return len(keys) == len(boxes)
