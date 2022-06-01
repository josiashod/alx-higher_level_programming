#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
last_digit = number % 10
print(f"Last digit of { number } is { last_digit  } and is { 'greater than 5' if last_digit > 5 else '0' if last_digit == 0 else 'less than 6 and not 0' }")