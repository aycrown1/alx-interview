#!/usr/bin/python3
"""
This module contains a program that that solves the N queens problem.
"""
import sys


def init():
    """
    Initialize the N value by checking command line arguments.

    Returns:
    int -- The validated N value.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)

    number = int(sys.argv[1])

    if number < 4:
        print("N must be at least 4")
        sys.exit(1)

    return number


def queenMoves(queen, column, previous):
    """
    Generate safe positions for the queen in the given column.

    Arguments:
    queen {int} -- The current queen's row.
    column {int} -- The current column.
    previous {List[List[int]]} -- List of previous solutions.

    Returns:
    List[List[int]] -- List of safe positions for the queen.
    """
    safe_position = []
    for array in previous:
        for index in range(column):
            if is_safe(queen, index, array):
                safe_position.append(array + [index])
    return safe_position


def generateMoves(row, column):
    """
    Generate all possible solutions for the N queens problem.

    Arguments:
    row {int} -- The number of queens to place.
    column {int} -- The current column.

    Returns:
    List[List[int]] -- List of all possible solutions.
    """
    solution = [[]]
    for queen in range(row):
        solution = queenMoves(queen, column, solution)
    return solution


def is_safe(q, x, array):
    """
    Check if placing a queen in the given position is safe.

    Arguments:
    q {int} -- The current queen's row.
    x {int} -- The current column.
    array {List[int]} -- The current partial solution.

    Returns:
    bool -- True if the position is safe, False otherwise.
    """
    if x in array:
        return False
    else:
        return all(abs(array[column] - x) != q - column for column in range(q))


def n_queens():
    """
    Solve the N queens problem and print solutions.
    """
    position = init()
    solutions = generateMoves(position, position)
    for array in solutions:
        clean = [[q, x] for q, x in enumerate(array)]
        print(clean)


if __name__ == '__main__':
    n_queens()
