#!/usr/bin/python3
def weight_average(my_list=[]):
    score = 0
    weight = 0

    for _tuple in my_list:
        score += _tuple[0] * _tuple[1]
        weight += _tuple[1]
    return (score / weight)
