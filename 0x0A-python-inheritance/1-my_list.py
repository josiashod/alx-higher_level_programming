#!/usr/bin/python3
"""MyList module"""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""

        print(sorted(self))
