#!/usr/bin/python3
def safe_print_division(value):
    """Prints an integer with "{:d}".format()."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return (False)
