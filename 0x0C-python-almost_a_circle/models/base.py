#!/usr/bin/python3
"""Base module"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries

        Parameters:
            list_dictionaries (list): list of dictionaries
        """

        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"

        return (json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string

        Parameters:
            json_string (str): string representing a list of dictionaries
        """

        if json_string is None or len(json_string) == 0:
            return ([])

        return (json.loads(json_string))

    @classmethod
    def save_to_file(cls, list_objs):
        """ Returns the JSON string representation of list_dictionaries

        Parameters:
            list_objs (list): a list of instances who inherits of Base
            - example: list of Rectangle or list of Square instances
        """

        if list_objs is None:
            list_objs = []

        list_objs = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_objs)

        with open(f"{cls.__name__}.json", "w") as f:
            f.write(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already 

        Parameters:
            dictionary (dict): key/value (keyworded arguments)
        """

        _new = cls(0, 0)
        _new.update(**dictionary)

        return (_new)
