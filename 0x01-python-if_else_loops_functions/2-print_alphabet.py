#!/usr/bin/python3
i = 97
str = ''
while i < (97 + 26):
    str += f"{chr(i)}"
    i += 1
print(str, end='')