#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        print(number % 10, end='')
    else:
        number = number * -1
        print(-1 * (number % 10), end='')
