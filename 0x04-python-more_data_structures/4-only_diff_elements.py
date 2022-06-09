#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Function that that returns a
    set of all elements present in only one set.
    """
    _list = []
    for i in list(filter(lambda x: x not in set_2, set_1)):
        _list.append(i)
    for i in list(filter(lambda x: x not in set_1 and x not in _list, set_2)):
        _list.append(i)
    return (_list)
