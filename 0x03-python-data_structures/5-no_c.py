#!/usr/bin/python3
def no_c(my_string):
    """Remove all characters c and C from a string."""
    for i in range(len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            my_string = my_string[:i] + " " + my_string[i+1:]
    return (my_string)
