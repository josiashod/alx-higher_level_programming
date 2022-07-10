#!/usr/bin/python3
""" Module for test Base class """
import os
import unittest
from io import StringIO
from unittest.mock import patch

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseMethods(unittest.TestCase):
    """ Suite to test Base class """

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_id(self):
        """ Test assigned id """
        new = Base(1)
        self.assertEqual(new.id, 1)

    def test_id_default(self):
        """ Test default id """
        new = Base()
        self.assertEqual(new.id, 1)

    def test_id_nb_objects(self):
        """ Test nb object attribute """
        new = Base()
        new2 = Base()
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 2)
        self.assertEqual(new3.id, 3)

    def test_id_mix(self):
        """ Test nb object attributes and assigned id """
        new = Base()
        new2 = Base(1024)
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 1024)
        self.assertEqual(new3.id, 2)

    def test_string_id(self):
        """ Test string id """
        new = Base('1')
        self.assertEqual(new.id, '1')

    def test_more_args_id(self):
        """ Test passing more args to init method """
        with self.assertRaises(TypeError):
            new = Base(1, 1)

    def test_access_private_attrs(self):
        """ Test accessing to private attributes """
        new = Base()
        with self.assertRaises(AttributeError):
            new.__nb_objects

    def test_to_json_string(self):
        """ Test convert json into string """

        r1 = Rectangle(10, 7, 2, 8)
        s1 = Square(10, 7, 2)

        tests = [
            f"[{str(r1.to_dictionary())}]",
            f"[{str(s1.to_dictionary())}]",
            f"[{str(r1.to_dictionary())}, {str(s1.to_dictionary())}]"
        ]
        equal_to = [
            Base.to_json_string([r1.to_dictionary()]),
            Base.to_json_string([s1.to_dictionary()]),
            Base.to_json_string([r1.to_dictionary(), s1.to_dictionary()])
        ]

        for i in range(3):
            self.assertEqual(equal_to[i], tests[i].replace("'", "\""))

    def test_save_to_file_1(self):
        """ Test JSON file """

        Square.save_to_file(None)
        res = "[]\n"
        with open("Square.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)

        try:
            os.remove("Square.json")
        finally:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_2(self):
        """ Test JSON file """

        Rectangle.save_to_file(None)
        res = "[]\n"
        with open("Rectangle.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)
        try:
            os.remove("Rectangle.json")
        finally:
            pass

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_from_json_string(self):
        """ Test JSON file """

        r1 = Rectangle(10, 7, 2, 8)
        s1 = Square(10, 7, 2)

        tests = [
            [r1.to_dictionary()],
            [s1.to_dictionary()],
            [r1.to_dictionary(), s1.to_dictionary()]
        ]

        equal_to = [
            Base.to_json_string([r1.to_dictionary()]),
            Base.to_json_string([s1.to_dictionary()]),
            Base.to_json_string([r1.to_dictionary(), s1.to_dictionary()])
        ]

        # convert it into list
        equal_to = [Base.from_json_string(el) for el in equal_to]

        for i in range(3):
            self.assertEqual(equal_to[i], tests[i])

    def test_create(self):
        """ Test object creation """

        r1 = Rectangle(10, 7, 2, 8)
        s1 = Square(10, 7, 2)

        r2 = Rectangle.create(width=10, height=7, x=2, y=8)
        s2 = Square.create(size=10, x=7, y=2)


        self.assertEqual(r1.width, r2.width)
        self.assertEqual(r1.height, r2.height)
        self.assertEqual(r1.x, r2.x)
        self.assertEqual(r1.y, r2.y)

        self.assertEqual(s1.size, s2.size)
        self.assertEqual(s1.x, s2.x)
        self.assertEqual(s1.y, s2.y)
