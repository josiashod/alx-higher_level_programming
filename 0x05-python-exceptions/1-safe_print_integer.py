#!/usr/bin/python3
def safe_print_integer(value):
    """Prints an integer with "{:d}".format()."""
    try:
        value = int(value)
    except ValueError:
        return (False)

    print("{:d}".format(value))
    return (True)
