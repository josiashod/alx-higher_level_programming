#!/usr/bin/python3
""" Module for test Square class """
import csv
import os
import unittest
from io import StringIO
from unittest.mock import patch

from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Suite to test Square class """

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0
        self.square = Square(4)

    def test_new_square(self):
        """ Test new square """
        new = Square(1, 1)
        self.assertEqual(new.size, 1)
        self.assertEqual(new.x, 1)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 2)

    def test_new_square_2(self):
        """ Test new square with all attrs """
        new = Square(2, 5, 5, 4)
        self.assertEqual(new.size, 2)
        self.assertEqual(new.x, 5)
        self.assertEqual(new.y, 5)
        self.assertEqual(new.id, 4)

    def test_new_squares(self):
        """ Test new squares """
        new = Square(1, 1)
        new2 = Square(1, 1)
        self.assertEqual(False, new is new2)
        self.assertEqual(False, new.id == new2.id)

    def test_is_Base_instance(self):
        """ Test Square is a Base instance """
        new = Square(1, 1)
        self.assertEqual(True, isinstance(new, Base))

    def test_incorrect_amount_attrs_1(self):
        """ Test error raised with no args passed """
        with self.assertRaises(TypeError):
            new = Square()

    def test_access_private_attrs(self):
        """ Trying to access to a private attribute """
        new = Square(1)
        with self.assertRaises(AttributeError):
            new.__size

    def test_access_private_attrs_3(self):
        """ Trying to access to a private attribute """
        new = Square(1, 1)
        with self.assertRaises(AttributeError):
            new.__x

    def test_access_private_attrs_4(self):
        """ Trying to access to a private attribute """
        new = Square(1, 1)
        with self.assertRaises(AttributeError):
            new.__y

    def test_valide_attrs(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            new = Square("2", 2, 2, 2)

    def test_valide_attrs_2(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            new = Square(2, "2", 2, 2)

    def test_valide_attrs_3(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            new = Square(2, 2, "2", 2)

    def test_value_attrs_1(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            new = Square(-1, 1, 1)

    def test_value_attrs_2(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            new = Square(1, 1, -1)

    def test_value_attrs_3(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            new = Square(1, -1, 1)

    def test_area(self):
        """ Trying to validate area of the square """

        new = Square(4)
        self.assertEqual(16, new.area())

    def test_display(self):
        """ Test string printed """
        r1 = Square(4)
        res = "####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display_2(self):
        """ Test string printed """

        r1 = Square(2)
        res = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_square_str_empty(self):
        """ Trying to test the output of the str of a square """

        self.assertEqual("[Square] (1) 0/0 - 4", str(self.square))

    def test_square_update_1(self):
        """ Trying to test update of the square """

        self.square.update(10, 4, 5, 6)

        self.assertEqual(self.square.id, 10)
        self.assertEqual(self.square.width, 4)
        self.assertEqual(self.square.height, 4)
        self.assertEqual(self.square.x, 5)
        self.assertEqual(self.square.y, 6)

    def test_square_update_2(self):
        """ Trying to test update of the square """

        self.square.update(id=10, size=4, x=6, y=5)

        self.assertEqual(self.square.id, 10)
        self.assertEqual(self.square.height, 4)
        self.assertEqual(self.square.width, 4)
        self.assertEqual(self.square.y, 5)
        self.assertEqual(self.square.x, 6)

    def test_to_dictionary(self):
        """ Test dictionary returned """

        r1 = Square(2, 3, 4, 1)
        res = "[Square] (1) 3/4 - 2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        self.assertEqual(r1.size, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 1)

        res = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(r1.to_dictionary()))
            self.assertEqual(str_out.getvalue(), res)

        res = "{'id': 1, 'size': 2, 'x': 3, 'y': 4}\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1.to_dictionary())
            self.assertEqual(str_out.getvalue(), res)

    def test_to_dictionary_2(self):
        """ Test dictionary returned """

        r1 = Square(2, 2, 2)
        res = "[Square] (2) 2/2 - 2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        r2 = Square(5)
        res = "[Square] (3) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r2)
            self.assertEqual(str_out.getvalue(), res)

        r1_dictionary = r1.to_dictionary()
        r2.update(**r1_dictionary)

        self.assertEqual(r1.size, r2.size)
        self.assertEqual(r1.x, r2.x)
        self.assertEqual(r1.y, r2.y)
        self.assertEqual(r1.id, r2.id)

        res = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(r1_dictionary))
            self.assertEqual(str_out.getvalue(), res)

        res = "{'id': 2, 'size': 2, 'x': 2, 'y': 2}\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1_dictionary)
            self.assertEqual(str_out.getvalue(), res)

    def test_create(self):
        """ Test create method """
        dictionary = {'id': 89}
        s1 = Square.create(**dictionary)
        self.assertEqual(s1.id, 89)

    def test_create_2(self):
        """ Test create method """
        dictionary = {'id': 89, 'size': 1}
        s1 = Square.create(**dictionary)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)

    def test_create_3(self):
        """ Test create method """
        dictionary = {'id': 89, 'size': 1, 'x': 2}
        s1 = Square.create(**dictionary)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)

    def test_create_4(self):
        """ Test create method """
        dictionary = {'id': 89, 'size': 1, 'x': 2, 'y': 3}
        s1 = Square.create(**dictionary)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)

    def test_load_from_file_2(self):
        """ Test load JSON file """
        s1 = Square(5)
        s2 = Square(8, 2, 5)

        linput = [s1, s2]
        Square.save_to_file(linput)
        loutput = Square.load_from_file()

        for i in range(len(linput)):
            self.assertEqual(linput[i].__str__(), loutput[i].__str__())
        
        try:
            os.remove("Square.json")
        finally:
            pass

    def test_csv_1(self):
        """ Test CSV file conversion """

        Square.save_to_file_csv([])
        res = [['id', 'size', 'x', 'y']]
        with open("Square.csv", "r") as file:
            self.assertEqual(list(csv.reader(file)), res)
        try:
            os.remove("Square.csv")
        finally:
            pass

        Square.save_to_file_csv(None)
        res = [['id', 'size', 'x', 'y']]
        with open("Square.csv", "r") as file:
            self.assertEqual(list(csv.reader(file)), res)
        try:
            os.remove("Square.csv")
        finally:
            pass

    def test_csv_2(self):
        """ Test load JSON file """

        r1 = Square(5)
        r2 = Square(8, 2, 5)

        Square.save_to_file_csv([r1])
        res = [['id', 'size', 'x', 'y'], ['2', '5', '0', '0']]
        with open("Square.csv", "r") as file:
            self.assertEqual(list(csv.reader(file)), res)
        try:
            os.remove("Square.csv")
        finally:
            pass

        Square.save_to_file_csv([r2])
        res = [['id', 'size', 'x', 'y'], ['3', '8', '2', '5']]
        with open("Square.csv", "r") as file:
            self.assertEqual(list(csv.reader(file)), res)
        try:
            os.remove("Square.csv")
        finally:
            pass

        Square.save_to_file_csv([r1, r2])
        res = [
            ['id', 'size', 'x', 'y'],
            ['2', '5', '0', '0'],
            ['3', '8', '2', '5']
        ]
        with open("Square.csv", "r") as file:
            self.assertEqual(list(csv.reader(file)), res)
        try:
            os.remove("Square.csv")
        finally:
            pass

    # def test_load_from_file_csv(self):
    #     """ Test load CSV file """
    #     s1 = Square(5)
    #     s2 = Square(8, 2, 5)

    #     linput = [s1, s2]
    #     Square.save_to_file_csv(linput)
    #     loutput = Square.load_from_file_csv()

    #     for i in range(len(linput)):
    #         self.assertEqual(linput[i].__str__(), loutput[i].__str__())
        
    #     try:
    #         os.remove("Square.csv")
    #     finally:
    #         pass
