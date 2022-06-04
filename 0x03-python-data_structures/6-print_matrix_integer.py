#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers."""
    if len(matrix) > 1:
        for line in matrix:
            _len = len(line)
            for i in range(_len):
                print("{:d}".format(line[i]), end="")
                if i != _len - 1:
                    print(" ", end="")
                else:
                    print()
    else:
        print()
