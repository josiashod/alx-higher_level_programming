#!/usr/bin/python3
for i in range(0, 100):
    if i != 99:
        print(f"{ i if i >= 10 else '0' + str(i) }", end=", ")
    else:
        print(i)
