#!/usr/bin/python3
"""
This module provides a function to generate Pascal's triangle up to the nth row.
"""
def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.
    
    Parameters:
    - n (int): The number of rows to generate.
    
    Returns:
    - list of lists: A list containing lists of integers representing Pascal's triangle.
    """
    if n <= 0:
        return []
    
    triangle = [[1]]
    
    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]
        
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])
        
        new_row.append(1)
        triangle.append(new_row)
    
    return triangle
