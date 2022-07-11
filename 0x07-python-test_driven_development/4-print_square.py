#!/usr/bin/python3
"""This is the integer addtion module.
>>> print_square("Billy")
Traceback (most recent call last):
    ...
TypeError: size must be an integer"""


def print_square(size):
    """function that prints a square with the character #
    >>> print_square(1)
    #"""

    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        return

    _print = ""
    for i in range(size):
        _print += "#" * size + ("\n" if i != (size - 1) else "")
    print(_print)
