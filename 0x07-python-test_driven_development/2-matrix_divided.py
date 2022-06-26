#!/usr/bin/python3
"""
This is the matrix division module.
"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix."""

    line_size = len(matrix[0])
    for line in matrix:
        if line_size != len(line):
            raise TypeError("Each row of the matrix must have the same size")
        for i in line:
            if type(i) != int and type(i) != float:
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for line in matrix:
        new_matrix.append(list(map(lambda x: round(x / div, 2), line)))
    return (new_matrix)
