#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments"""
    from sys import argv

    _len = len(argv) - 1
    _end = 's:' if _len > 1 else ':' if _len == 1 else 's.'
    print("{} argument{}".format(_len, _end))
    for i in range(1, _len + 1):
        print("{}: {}".format(i, argv[i]))
