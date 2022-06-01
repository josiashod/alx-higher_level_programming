#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
last_digit = number % 10
str = f"Last digit of { number } is { last_digit  } and is "
if last_digit > 5:
    str += "greater than 5"
elif last_digit == 0:
    str += '0'
else:
    str += 'less than 6 and not 0'
print(str)