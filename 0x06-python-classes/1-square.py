#!/usr/bin/python3
"""Defines class Square
"""


class Square():
    """Square class

    Args:
        size: The size of the square

    """

    def __init__(self, size: int) -> None:
        """Init of an instance of squere.

        Args:
            size (int): The size of the square
        """
        self.__size = size
