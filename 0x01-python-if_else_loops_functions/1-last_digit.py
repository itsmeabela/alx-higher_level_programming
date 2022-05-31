#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number2 = (((number * -1) % 10) * -1)
else:
    number2 = number % 10
print("Last digit of {:d} is {:d}".format(number, number2), end=' ')
if number2 > 5:
    print("and is greater than 5")
elif number2 == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
