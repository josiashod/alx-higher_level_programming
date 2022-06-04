#!/usr/bin/python3
def new_in_list(my_list, idx, new_element):
    """Replace an element of a list at
    a specific position without modifying
    the original list (like in C).
    """
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    new_list = list(my_list)
    new_list[idx] = new_element
    return (new_list)
