#!/usr/bin/python3
"""Defines class Square"""


class Square():
    """Square class

    Args:
        size: The size of the square

    """

    def __init__(self, size=0, position=(0, 0)):
        """Init of an instance of squere.

        Args:
            size (int): The size of the square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, position):
        if (type(position) is not tuple) or (len(position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(position[0]) is not int) or (type(position[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (position[0] < 0) or (position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """Give the current square area"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints in stdout the square with the character #"""

        _print = ""
        if self.__size != 0:
            _print += "\n" * self.position[1]
        for i in range(self.size):
            _print += " " * self.position[0]
            _print += "#" * self.size + ("\n" if i < self.size - 1 else "")
        print(_print)
