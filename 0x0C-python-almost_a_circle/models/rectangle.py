#!/usr/bin/python3
""" Module that contains class Rectangle,
inheritance of class Base
"""
from models.base import Base


class Rectangle(Base):
    """This class represent a Rectangle

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
        __x (int): The x value.
        __y (int): The y value.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        The constructor for Rectangle class.

        Parameters:
           width (int): The width of the rectangle.
           height (int): The height of the rectangle.
           x (int): The x value.
           y (int): The y value.
           id (int): the id of the object created.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """The getter of the attribute __width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """The getter of the attribute __height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """The getter of the attribute __x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """The getter of the attribute __y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Return the area of the rectangle"""

        return (self.__width * self.__height)

    def display(self):
        """ Display the rectangle """

        _print = ""
        if self.__height > 0 and self.__width > 0:
            _print += "\n" * self.__y
            for i in range(self.__height):
                _print += " " * self.__x
                _print += "#" * self.__width
                if i != (self.__height - 1):
                    _print += "\n"
        print(_print)

    def update(self, *args, **kwargs):
        """ Update rectangle object with an array of argument

        Parameters:
            *args (list): list of arguments
                1st argument: should be the id attribute
                2nd argument: should be the width attribute
                3rd argument: should be the height attribute
                4th argument: should be the x attribute
                5th argument: should be the y attribute
            **kwargs (dict): dictionnary of arguments
                width (int): The width of the rectangle.
                height (int): The height of the rectangle.
                x (int): The x value.
                y (int): The y value.
                id (int): the id of the object created.
        """

        if args is not None and len(args) != 0:
            list_attr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Return the dictionary representation of a Rectangle """

        _attrs = ['id', 'width', 'height', 'x', 'y']
        _dict = {}
        for attr in _attrs:
            _dict[attr] = getattr(self, attr)

        return (_dict)

    def __str__(self):
        """ Return the str of the Rectangle """

        _str = "[Rectangle] "
        _str += f"({self.id}) {self.x}/{self.y}"
        _str += f" - {self.width}/{self.height}"

        return (_str)
