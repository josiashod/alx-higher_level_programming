#!/usr/bin/python3
""" Module for test Rectangle class """
import csv
import os
import unittest
from io import StringIO
from unittest.mock import patch

from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Suite to test Rectangle class """

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0
        self.rectangle = Rectangle(4, 2)

    def test_new_rectangle(self):
        """ Test new rectangle """
        new = Rectangle(1, 1)
        self.assertEqual(new.width, 1)
        self.assertEqual(new.height, 1)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 2)

    def test_new_rectangle_2(self):
        """ Test new rectangle with all attrs """
        new = Rectangle(2, 3, 5, 5, 4)
        self.assertEqual(new.width, 2)
        self.assertEqual(new.height, 3)
        self.assertEqual(new.x, 5)
        self.assertEqual(new.y, 5)
        self.assertEqual(new.id, 4)

    def test_new_rectangles(self):
        """ Test new rectangles """
        new = Rectangle(1, 1)
        new2 = Rectangle(1, 1)
        self.assertEqual(False, new is new2)
        self.assertEqual(False, new.id == new2.id)

    def test_is_Base_instance(self):
        """ Test Rectangle is a Base instance """
        new = Rectangle(1, 1)
        self.assertEqual(True, isinstance(new, Base))

    def test_incorrect_amount_attrs(self):
        """ Test error raise with 1 arg passed """
        with self.assertRaises(TypeError):
            new = Rectangle(1)

    def test_incorrect_amount_attrs_1(self):
        """ Test error raised with no args passed """
        with self.assertRaises(TypeError):
            new = Rectangle()

    def test_access_private_attrs(self):
        """ Trying to access to a private attribute """
        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__width

    def test_access_private_attrs_2(self):
        """ Trying to access to a private attribute """
        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__height

    def test_access_private_attrs_3(self):
        """ Trying to access to a private attribute """
        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__x

    def test_access_private_attrs_4(self):
        """ Trying to access to a private attribute """
        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__y

    def test_valide_attrs(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            new = Rectangle("2", 2, 2, 2, 2)

    def test_valide_attrs_2(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            new = Rectangle(2, "2", 2, 2, 2)

    def test_valide_attrs_3(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            new = Rectangle(2, 2, "2", 2, 2)

    def test_valide_attrs_4(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            new = Rectangle(2, 2, 2, "2", 2)

    def test_value_attrs_2(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            new = Rectangle(1, 1, -1)

    def test_value_attrs_3(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            new = Rectangle(1, 1, 1, -1)

    def test_area(self):
        """ Trying to validate area of the rectangle """

        new = Rectangle(4, 8)
        self.assertEqual(32, new.area())

    def test_display(self):
        """ Test string printed """
        r1 = Rectangle(2, 5)
        res = "##\n##\n##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display_2(self):
        """ Test string printed """

        r1 = Rectangle(2, 2)
        res = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.width = 5
        res = "#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_rectangle_update_1(self):
        """ Trying to test update of the rectangle """

        self.rectangle.update(10, 3, 4, 5, 6)

        self.assertEqual(self.rectangle.id, 10)
        self.assertEqual(self.rectangle.width, 3)
        self.assertEqual(self.rectangle.height, 4)
        self.assertEqual(self.rectangle.x, 5)
        self.assertEqual(self.rectangle.y, 6)

    def test_rectangle_update_2(self):
        """ Trying to test update of the rectangle """

        self.rectangle.update(id=10, height=3, width=4, y=5, x=6)

        self.assertEqual(self.rectangle.id, 10)
        self.assertEqual(self.rectangle.height, 3)
        self.assertEqual(self.rectangle.width, 4)
        self.assertEqual(self.rectangle.y, 5)
        self.assertEqual(self.rectangle.x, 6)

    def test_to_dictionary(self):
        """ Test dictionary returned """

        r1 = Rectangle(1, 2, 3, 4, 1)
        res = "[Rectangle] (1) 3/4 - 1/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 1)

        res = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(r1.to_dictionary()))
            self.assertEqual(str_out.getvalue(), res)

        res = "{'id': 1, 'width': 1, 'height': 2, 'x': 3, 'y': 4}\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1.to_dictionary())
            self.assertEqual(str_out.getvalue(), res)

    def test_to_dictionary_2(self):
        """ Test dictionary returned """

        r1 = Rectangle(2, 2, 2, 2)
        res = "[Rectangle] (2) 2/2 - 2/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        r2 = Rectangle(5, 7)
        res = "[Rectangle] (3) 0/0 - 5/7\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r2)
            self.assertEqual(str_out.getvalue(), res)

        r1_dictionary = r1.to_dictionary()
        r2.update(**r1_dictionary)

        self.assertEqual(r1.width, r2.width)
        self.assertEqual(r1.height, r2.height)
        self.assertEqual(r1.x, r2.x)
        self.assertEqual(r1.y, r2.y)
        self.assertEqual(r1.id, r2.id)

        res = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(r1_dictionary))
            self.assertEqual(str_out.getvalue(), res)

        res = "{'id': 2, 'width': 2, 'height': 2, 'x': 2, 'y': 2}\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1_dictionary)
            self.assertEqual(str_out.getvalue(), res)

    def test_create(self):
        """ Test create method """
        dictionary = {'id': 89}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)

    def test_create_2(self):
        """ Test create method """
        dictionary = {'id': 89, 'width': 1}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)

    def test_create_3(self):
        """ Test create method """
        dictionary = {'id': 89, 'width': 1, 'height': 2}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

    def test_create_4(self):
        """ Test create method """
        dictionary = {'id': 89, 'width': 1, 'height': 2, 'x': 3}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)

    def test_create_5(self):
        """ Test create method """
        dictionary = {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_load_from_file(self):
        """ Test load JSON file """
        load_file = Rectangle.load_from_file()
        self.assertEqual(load_file, [])

    def test_load_from_file_2(self):
        """ Test load JSON file """
        r1 = Rectangle(5, 5)
        r2 = Rectangle(8, 2, 5, 5)

        linput = [r1, r2]
        Rectangle.save_to_file(linput)
        loutput = Rectangle.load_from_file()

        for i in range(len(linput)):
            self.assertEqual(linput[i].__str__(), loutput[i].__str__())

        try:
            os.remove("Rectangle.json")
        finally:
            pass

    def test_csv_1(self):
        """ Test CSV file conversion """

        Rectangle.save_to_file_csv([])
        res = [['id', 'width', 'height', 'x', 'y']]
        with open("Rectangle.csv", "r") as file:
            self.assertEqual(list(csv.reader(file)), res)
        try:
            os.remove("Rectangle.csv")
        finally:
            pass

        Rectangle.save_to_file_csv(None)
        res = [['id', 'width', 'height', 'x', 'y']]
        with open("Rectangle.csv", "r") as file:
            self.assertEqual(list(csv.reader(file)), res)
        try:
            os.remove("Rectangle.csv")
        finally:
            pass

    def test_csv_2(self):
        """ Test load JSON file """

        r1 = Rectangle(5, 5)
        r2 = Rectangle(8, 2, 5, 5)

        Rectangle.save_to_file_csv([r1])
        res = [['id', 'width', 'height', 'x', 'y'], ['2', '5', '5', '0', '0']]
        with open("Rectangle.csv", "r") as file:
            self.assertEqual(list(csv.reader(file)), res)
        try:
            os.remove("Rectangle.csv")
        finally:
            pass

        Rectangle.save_to_file_csv([r2])
        res = [['id', 'width', 'height', 'x', 'y'], ['3', '8', '2', '5', '5']]
        with open("Rectangle.csv", "r") as file:
            self.assertEqual(list(csv.reader(file)), res)
        try:
            os.remove("Rectangle.csv")
        finally:
            pass

        Rectangle.save_to_file_csv([r1, r2])
        res = [
            ['id', 'width', 'height', 'x', 'y'],
            ['2', '5', '5', '0', '0'],
            ['3', '8', '2', '5', '5']
        ]
        with open("Rectangle.csv", "r") as file:
            self.assertEqual(list(csv.reader(file)), res)
        try:
            os.remove("Rectangle.csv")
        finally:
            pass

    def test_load_from_file_csv(self):
        """ Test load CSV file """
        r1 = Rectangle(5, 5)
        r2 = Rectangle(8, 2, 5, 5)

        linput = [r1, r2]
        Rectangle.save_to_file_csv(linput)
        loutput = Rectangle.load_from_file_csv()

        for i in range(len(linput)):
            self.assertEqual(linput[i].__str__(), loutput[i].__str__())

        try:
            os.remove("Rectangle.csv")
        finally:
            pass
