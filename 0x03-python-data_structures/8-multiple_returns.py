#!/usr/bin/python3
def multiple_returns(sentence):
    """Return a tuple with the length
    of a string and its first character.
    """
    _len = len(sentence)
    first_char = "None" if _len == 0 else sentence[0]

    return (_len, first_char)
