#!/usr/bin/python3
"""Base module"""
import json
import csv
import turtle


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
        """ Writes the JSON string representation of list_objs to a file

        Parameters:
            list_objs (list): a list of instances who inherits of Base
            - example: list of Rectangle or list of Square instances
        """

        if list_objs is None or len(list_objs) == 0:
            list_objs = []

        list_objs = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_objs)

        with open(f"{cls.__name__}.json", "w") as f:
            f.write(json_string)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serializes the list of object in CSV file

        Parameters:
            list_objs (list): a list of instances who inherits of Base
            - example: list of Rectangle or list of Square instances
        """

        if list_objs is None:
            with open(f"{cls.__name__}.csv", "w", newline='') as f:
                csv.writer(f).writerows([])
            return

        list_objs = [obj.to_dictionary() for obj in list_objs]

        with open(f"{cls.__name__}.csv", "w", newline='') as f:
            writer = csv.writer(f)

            if len(list_objs) > 0:
                header = list_objs[0].keys()
                writer.writerow(header)

            data = [obj.values() for obj in list_objs]
            writer.writerows(data)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already

        Parameters:
            dictionary (dict): key/value (keyworded arguments)
        """

        _new = cls(0, 0)
        _new.update(**dictionary)

        return (_new)

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """

        _list = []
        with open(f"{cls.__name__}.json") as f:
            _list = cls.from_json_string(f.read())
            _list = ([cls.create(**dic) for dic in _list])

        return (_list)

    @classmethod
    def load_from_file_csv(cls):
        """ Returns a list of instances """

        _list = []
        with open(f"{cls.__name__}.csv") as f:
            reader = list(csv.reader(f))
            header = reader[0]

            _list = []
            for i in range(1, len(reader)):
                dic = {}
                for j in range(len(header)):
                    dic[header[j]] = int(reader[i][j])

                _list.append(cls.create(**dic))

        return (_list)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Opens a window and draws all the Rectangles and Squares

        Parameters:
            list_rectangles (list): list of Rectangles
            list_squares (list): list of Square
        """

        turtle.title("0x0C. Python - Almost a circle")
        for rectangle in list_rectangles:
            for i in range(2):
                turtle.forward(rectangle.width)
                turtle.left(90)
                turtle.forward(rectangle.height)
                turtle.left(90)

        for square in list_squares:
            for i in range(4):
                turtle.forward(square.size)
                turtle.left(90)


        #calling for the mainloop()
        turtle.mainloop()