#!/usr/bin/python3
"""This is the integer addtion module.
>>> add_integer("b")
Traceback (most recent call last):
    ...
TypeError: a must be an integer"""


def add_integer(a, b=98):
    """Return the addtion of two integer
    >>> add_integer(45, 5)
    50"""

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
