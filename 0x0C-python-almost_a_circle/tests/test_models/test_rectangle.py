#!/usr/bin/python3
""" Module for test Rectangle class """
import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestRectangle(unittest.TestCase):
    """ Suite to test Rectangle class """

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0
        self.empty_rectangle = Rectangle(0, 0)
        self.rectangle = Rectangle(4, 2)

    def test_new_rectangle(self):
        """ Test new rectangle """
        new = Rectangle(1, 1)
        self.assertEqual(new.width, 1)
        self.assertEqual(new.height, 1)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 3)

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

    def test_rectangle_str_empty(self):
        """ Trying to test the output of the str of an empty rectangle """

        self.assertEqual("[Rectangle] (1) 0/0 - 0/0", str(self.empty_rectangle))

    def test_rectangle_str_empty(self):
        """ Trying to test the output of the str of a rectangle """

        self.assertEqual("[Rectangle] (2) 0/0 - 4/2", str(self.rectangle))

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
