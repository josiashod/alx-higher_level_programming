#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list."""

    nb_print = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            nb_print += 1
        except IndexError:
            continue
    print()
    return (nb_print)
