#!/usr/bin/python3
"""Defines a class named Square"""


class Square:
    """calculates the area of a square and prints it"""
    def __init__(self, size=0):
        """initializes the size of the square

        Args:
            size(int): size of the square

        Raises:
            TypeError: when size is not an integer
            ValueError: when size is less than 0
        """
        self.__size = size
        if not type(size) == int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
