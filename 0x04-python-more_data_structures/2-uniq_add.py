#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Function that adds all
    unique integers in a list
    (only once for each integer).
    """

    return sum(list(dict.fromkeys(my_list)))
