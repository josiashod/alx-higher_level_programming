#!/usr/bin/python3
""" Module that contains class Square,
inheritance of class Rectangle
"""
from numpy import size
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class represent a Square

    Attributes:
        __size (int): The size of the square.
        __x (int): The x value.
        __y (int): The y value.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        The constructor for Square class.

        Parameters:
           size (int): The size of the square.
           x (int): The x value.
           y (int): The y value.
           id (int): the id of the object created.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """The getter of the attribute size"""

        return (self.width)

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Update square object with an array of argument

        Parameters:
            *args (list): list of arguments
                1st argument: should be the id attribute
                2nd argument: should be the size attribute
                3rd argument: should be the x attribute
                4th argument: should be the y attribute
            **kwargs (dict): dictionnary of arguments
                size (int): The size of the square.
                x (int): The x value.
                y (int): The y value.
                id (int): the id of the object created.
        """

        if args is not None and len(args) != 0:
            list_attr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Return the dictionary representation of a Square """

        _attrs = ['id', 'size', 'x', 'y']
        _dict = {}
        for attr in _attrs:
            _dict[attr] = getattr(self, attr)

        return (_dict)

    def __str__(self):
        """ Return the str of the Square """

        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")
