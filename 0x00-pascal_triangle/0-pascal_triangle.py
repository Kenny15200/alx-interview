#!/usr/bin/python3

'''
    Creates a function that returns a list of lists of integers
    representing a Pascal's triangle for any given integer of n:
'''


def pascal_triangle(n):
    '''
        A function that creates a list of lists of integers representing
        the Pascal's triangle of n.
    '''
    triangle = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)

    return triangle
