#!/usr/bin/python3
"""Defines class Square
"""


class Square():
    """Square class

    Args:
        size: The size of the square

    """

    def __init__(self, size=0) -> None:
        """Init of an instance of squere.

        Args:
            size (int): The size of the square
        """
        try:
            size = int(size)
        except TypeError:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
