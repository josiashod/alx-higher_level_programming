#!/usr/bin/python3
def roman_to_int(roman_string):
    """Function that converts a Roman numeral to an integer."""

    symbols = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    _prev = 0
    number = 0
    if type(roman_string) != str or not roman_string:
        return (0)

    for letter in roman_string:
        value = symbols[letter]
        number += value

        if _prev != 0 and _prev < value:
            number -= _prev * 2

        _prev = symbols[letter]
    return (number)
