#!/usr/bin/python3
"""
This module is an interveiw challenge
project that rotates a 2D matrix
"""


def rotate_2d_matrix(matrix):
    """
    This function rotate it 90 degrees clockwise
    given an n x n 2D matrix

    This process involves transpose of the matrix
    and reverse of each row to achieve the 90-degree
    rotation
    """
    row = len(matrix)

    for i in range(row):
        for j in range(i, row):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(row):
        matrix[i].reverse()
