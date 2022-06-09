#!/usr/bin/python3
def best_score(a_dictionary):
    """Function that returns a key with the biggest integer value."""

    if a_dictionary is None:
        return ("None")
    _max = max(a_dictionary.values())
    _max = [k for k, v in a_dictionary.items() if v == _max]
    return _max[0]
