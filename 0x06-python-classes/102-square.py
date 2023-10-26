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
        if type(size) != int and type(size) != float:
            raise TypeError('size must be a number')
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
        """sets the value of size

        Args:
            size(int): size of the square
        """
        if not type(size) == int and type(size) != float:
            raise TypeError('size must be a number')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def __gt__(self, other):
        """Compares the area of two squares to determine which is
        bigger than the other
        """
        return (self.area() > other.area())

    def __lt__(self, other):
        """Compares the area of two squares to determine which is
        smaller than the other.
        """
        return (self.area() < other.area())

    def __eq__(self, other):
        """Compares the area of two squares to deterrmine if both squares are
        equal in size
        """
        return (self.area() == other.area())

    def __ne__(self, other):
        """compares the area of two squares to determine if the squares
        are not equal to each other
        """
        return (self.area() != other.area())

    def __ge__(self, other):
        """Compares the area of two squares to determine if one greater
        or equal to the other in size
        """
        return (self.area() >= other.area())

    def __le__(self, other):
        """Compares the area of two squares to determine f one is less than
        the other in size
        """
        return (self.area() <= other.area())
