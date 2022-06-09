#!/usr/bin/python3
def weight_average(my_list=[]):
    """Function that returns the weighted average
    of all integers tuple (<score>, <weight>)"""

    if not my_list:
        return (0)

    score = 0
    weight = 0

    for _tuple in my_list:
        score += _tuple[0] * _tuple[1]
        weight += _tuple[1]
    return (score / weight)
