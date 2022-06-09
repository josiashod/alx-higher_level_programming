#!/usr/bin/python3
def best_score(a_dictionary):
    """Function that returns a key with the biggest integer value."""

    if a_dictionary is None:
        return ("None")
    _values = list(a_dictionary.values())
    _keys = list(a_dictionary.keys())
    return (_keys[_values.index(max(_values))])
