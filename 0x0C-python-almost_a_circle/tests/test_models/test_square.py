#!/usr/bin/python3
""" Module for test Square class """
import unittest
from models.square import Square
from models.base import Base

class TestSquare(unittest.TestCase):
    """ Suite to test Square class """

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0
        self.empty_square = Square(0)
        self.square = Square(4)

    def test_new_square(self):
        """ Test new square """
        new = Square(1, 1)
        self.assertEqual(new.size, 1)
        self.assertEqual(new.x, 1)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 3)

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

    def test_square_str_empty(self):
        """ Trying to test the output of the str of an empty square """

        self.assertEqual("[Square] (1) 0/0 - 0", str(self.empty_square))

    def test_square_str_empty(self):
        """ Trying to test the output of the str of a square """

        self.assertEqual("[Square] (2) 0/0 - 4", str(self.square))
