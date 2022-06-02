#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    _len = len(argv)
    print("{} arguments:".format(_len - 1))
    for i in range(1, _len):
        print("{}: {}".format(i, argv[i]))
