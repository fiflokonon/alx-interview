#!/usr/bin/python3
"""
0-pascal_triangle module
This module contains the function pascal_triangle(n) that returns
a list of lists of integers representing Pascal's Triangle of n.
"""
def pascal_triangle(n):
    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # Generate each row of Pascal's Triangle
    for i in range(1, n):
        # Start the row with a 1
        row = [1]
        # Generate the middle values by summing elements from the previous row
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        # End the row with a 1
        row.append(1)
        # Add the row to the triangle
        triangle.append(row)
    
    return triangle

