#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a list and only integers."""

    nb_print = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (IndexError, ValueError, TypeError):
            continue
        else:
            nb_print += 1
    print()
    return (nb_print)
