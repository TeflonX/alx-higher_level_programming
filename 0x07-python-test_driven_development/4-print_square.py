#!/usr/bin/python3
def print_square(size):
    if not type(size) is int:
        raise TypeError('size must be an integer')
    if size < 0:
        ValueError('size must be >= 0')

    for x in range(size):
        print('#' * size, end='')
        print()
