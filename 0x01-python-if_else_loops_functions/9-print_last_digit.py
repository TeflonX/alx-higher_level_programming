#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        print(number % 10, end='')
        return number % 10
    else:
        number *= -1
        number = number % 10
        print(number, end='')
        return (number % 10)
