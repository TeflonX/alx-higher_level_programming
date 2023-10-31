#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    new_num = (-1 * number) % 10
    if (new_num % 10) > 0 and (new_num % 10) < 6:
        print("Last digit of {} is {} and is less than 6 and not 0"
            .format(number,-1 * new_num)
    if new_num == 0:
        print("Last digit of {} is {} and is 0".format(number, new_num)

if number >= 0:
    if (number % 10) > 5:
        print("Last digit of {} is {} and is greater than 5"
        .format(number, number % 10)
    elif (number % 10) == 0:
        print("Last digit of {} is {} and is 0".format(number, number % 10)
    elif (number % 10) > 0 and (number % 10) < 6:
    print("Last digit of {} is {} and is less than 6 and not 0"
        .format(number, number % 10)
