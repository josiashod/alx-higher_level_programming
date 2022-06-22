#!/usr/bin/python3
"""Defines class Square
"""


from turtle import position


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
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, position):
        if (type(position) != tuple) or (len(position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) != int and type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 and position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """Give the current square area"""
        return (self.__size**2)

    def my_print(self):
        """Prints in stdout the square with the character #"""

        _print = ""
        _print += "\n" * self.__position[1]
        for i in range(self.__size):
            _print += " " * self.__position[0]
            _print += "#" * self.__size
            if i != (self.__size - 1):
                _print += "\n"
        print(_print)
