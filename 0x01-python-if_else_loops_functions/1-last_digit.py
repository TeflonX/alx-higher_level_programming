#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    positive_num = number * -1
    print("Last digit of", number, "is", -1 * (positive_num % 10))
else:
    print("Last digit of", number, "is", number % 10)
