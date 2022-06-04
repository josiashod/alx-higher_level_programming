#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers."""
    for line in matrix:
        for i in range(len(line)):
            if i != 0:
                print(" ", end="")
            print("{:d}".format(line[i]), end="")
        print()
