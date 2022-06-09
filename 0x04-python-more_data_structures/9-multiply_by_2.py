#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Function that returns a new dictionary
    with all values multiplied by 2."""

    _new_dict = dict()
    for key, value in a_dictionary.items():
        _new_dict[key] = value * 2
    return (_new_dict)
