#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    _list = dir(hidden_4)
    for item in _list:
        if item[0] != "_":
            print("{}".format(item))
