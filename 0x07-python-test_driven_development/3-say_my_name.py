#!/usr/bin/python3
"""This is the integer addtion module.
>>> say_my_name(12, "Billy")
Traceback (most recent call last):
    ...
TypeError: first_name must be a string"""


def say_my_name(first_name, last_name=""):
    """function that prints My name is <first name> <last name>
    >>> say_my_name("Josh")
     My name is Josh"""

    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
