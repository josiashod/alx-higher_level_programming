#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Function that computes the square
    value of all integers of a matrix.
    """

    new_list = []
    for line in matrix:
        new_list.append(list(map(lambda x: x**2, line)))

    return new_list
