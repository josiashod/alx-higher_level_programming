#!/usr/bin/python3
"""The Rectangle module"""


class Rectangle():
    """Rectangle class
    Attr:
        number_of_instances (int): the number of Rectangle instance
        print_symbol (str): the symbol use to print the rectangle
        width (int): the width of the rectangle
        height (int): the height of the rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
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
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area
        Attr:
            rect_1 (Rectangle): the first rectangle
            rect_2 (Rectangle): the second rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        return (rect_1 if (rect_1.area() >= rect_2.area()) else rect_2)

    def __str__(self) -> str:
        """Print the rectangle with the character #"""

        _print = ""
        for i in range(self.__height):
            _print += str(self.print_symbol) * self.__width
            if i != (self.__height - 1):
                _print += "\n"
        return (_print)

    def __repr__(self) -> str:
        """Return a string representation of the rectangle to
        be able to recreate a new instance by using eval()"""

        return (f"Rectangle({self.width}, {self.height})")

    def __del__(self) -> None:
        """Print a message when an instance of Rectangle is deleted"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
