#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        _ord = ord(str[i])
        if _ord >= 97 and _ord <= 122:
            str = str[:i] + chr(_ord - 32) + str[(i + 1):]
    print("{}".format(str))
    
