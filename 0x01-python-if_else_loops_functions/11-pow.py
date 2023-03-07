#!/usr/bin/python3
def pow(a, b):
    # a program that prints a raise to power b
    count = 1
    if b < 0:
        b = -1 * b
        for i in range(b):
            count = a * count
        count = 1 / count
        return (count)

    for i in range(b):
        count = a * count
    return (count)
