#!/usr/bin/python3
"""Interview about a function that returns the perimeter of the island described in grid
"""


def check(x):
    """Check the value of x and return 1 if it's 0, otherwise 0.
    """
    return 1 if x == 0 else 0


def island_perimeter(grid):
    """Calculate the perimeter of the island in the given grid."""
    row = len(grid)
    col = len(grid[0])
    assert 1 <= row <= 100 and 1 <= col <= 100,
    "Length must be between 1 and 100"

    x = 0
    for i in range(row):
        for j in range(col):
            assert grid[i][j] in {0, 1}, "Grid numbers must be 0 or 1"
            if grid[i][j] == 1:
                x += 1 if i - 1 < 0 else check(grid[i - 1][j])
                x += 1 if j - 1 < 0 else check(grid[i][j - 1])

                try:
                    x += check(grid[i + 1][j])
                except IndexError:
                    x += 1

                try:
                    x += check(grid[i][j + 1])
                except IndexError:
                    x += 1

    return x
