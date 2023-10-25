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

    def area(self):
        """Calculates the area of the square

        Returns:
            area: area of the square
        """
        area = (self.__size) * (self.__size)
        return (area)

    @property
    def size(self):
        """retrieves the value of the private attribute, size

        Return:
            size(int): size of square
        """
        return self.__size

    @size.setter
    def size(self, size):
        """sets the value of size"""
        if not type(size) == int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
