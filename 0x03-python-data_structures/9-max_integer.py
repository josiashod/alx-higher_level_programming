#!/usr/bin/python3
from audioop import reverse


def max_integer(my_list=[]):
    """Find the biggest integer of a list."""
    _len = len(my_list)
    my_list.sort(reverse= True)
    return ("None" if _len == 0 else my_list[0])
