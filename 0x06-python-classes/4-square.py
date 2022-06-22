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
        self.__size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Give the current square area"""
        return (self.__size**2)
