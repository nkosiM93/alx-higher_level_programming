#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    ld = abs(number)
    ld %= 10
    ld *= -1
else:
    ld = number % 10  # Last digit

print(f"Last digit of {number:d} is {ld:d} ", end="")

if ld > 5:
    print(f"and is greater than 5")
elif ld < 6 and ld != 0:
    print(f"and is less than 6 and not 0")
else:
    print(f"and is 0")
