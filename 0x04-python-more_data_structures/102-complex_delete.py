#!/usr/bin/python3
def complex_delete(a_dictionary, value=""):
    """Function that deletes keys with a specific value in a dictionary."""

    for i in [k for k, v in a_dictionary.items() if v == value]:
        del a_dictionary[i]
    return (a_dictionary)
