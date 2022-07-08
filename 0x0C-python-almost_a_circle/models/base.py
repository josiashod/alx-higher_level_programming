#!/usr/bin/python3
"""Base module"""


class Base:
    """This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes
    and to avoid duplicating the same code (by extension, same bugs)

    Attributes:
        __nb_objects (int): to know the number of object created
        id (int): to know the number of object created
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if not id:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
