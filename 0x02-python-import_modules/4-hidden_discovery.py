#!/usr/bin/python3
if __name__ == "__main__":
    """Print all the names defined by the compiled module hidden_4.pyc"""
    import hidden_4

    _list = dir(hidden_4)
    for item in _list:
        if item[0] != "_":
            print("{}".format(item))
