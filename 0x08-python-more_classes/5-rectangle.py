#!/usr/bin/python3
"""The Rectangle module"""


class Rectangle():
    """Rectangle class
    Attr:
        width (int): the width of the rectangle
        height (int): the height of the rectangle
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Return the area of the rectangle"""

        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the rectangle"""

        if (self.__width == 0) or (self.__height == 0):
            return (0)
        return ((self.__width + self.__height) * 2)

    def __str__(self) -> str:
        """Print the rectangle with the character #"""

        _print = ""
        for i in range(self.__height):
            _print += "#" * self.__width
            if i != (self.__height - 1):
                _print += "\n"
        return (_print)

    def __repr__(self) -> str:
        """Return a string representation of the rectangle to
        be able to recreate a new instance by using eval()"""

        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self) -> None:
        """Print a message when an instance of Rectangle is deleted"""

        print("Bye rectangle...")
