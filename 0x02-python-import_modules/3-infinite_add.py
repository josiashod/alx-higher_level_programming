#!/usr/bin/python3
if __name__ == "__main__":
    """Print the result of the addition of all arguments"""
    from sys import argv

    _len = len(argv)
    sum = 0
    for i in range(1, _len):
        sum += int(argv[i])
    print("{}".format(sum))
