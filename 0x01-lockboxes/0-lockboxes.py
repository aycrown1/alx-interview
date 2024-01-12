#!/usr/bin/python3
"""
This module is an interview challenge in python
"""


def canUnlockAll(boxes):
    """
    canUnlockAll function determines if all the boxes can be opened
    """
    keys = set([0])
    opened_boxes = set()

    while keys:
        current_key = keys.pop()
        opened_boxes.add(current_key)

        current_box = boxes[current_key]
        keys.update(set(current_box) - opened_boxes)

    return len(opened_boxes) == len(boxes)
