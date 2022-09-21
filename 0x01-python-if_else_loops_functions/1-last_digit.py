#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

try:
    last = (abs(number) % 10) * int(number / abs(number))
except ZeroDivisionError:
    last = 0

if last > 5:
    report = "and is greater than 5"
elif last == 0:
    report = "and is 0"
else:
    report = "and is less than 6 and not 0"

print(f"Last digit of {number} is {last} {report}")
