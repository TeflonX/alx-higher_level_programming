#!/usr/bin/python3
"""Defines a class named Square"""


class Square:
    """calculates the area of a square and prints it"""
    def __init__(self, size=0, position=(0, 0)):
        """initializes the size of the square

        Args:
            size(int): size of the square

        Raises:
            TypeError: when size is not an integer
            ValueError: when size is less than 0
        """
        self.__size = size
        self.__position = position
        if not type(size) == int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        if not type(position) == tuple or len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if not all(isinstance(x, int) for x in position):
            raise TypeError('position must be a tuple of 2 positive integers')
        if not all(x >= 0 for x in position):
            raise TypeError('position must be a tuple of 2 positive integers')

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
        if not type(size) == int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def my_print(self):
        """prints the square using '#'"""
        if self.__size == 0:
            print()
        else:
            for x in range(self.__position[1]):
                print('')
            for i in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size, end='')
                print()

    @property
    def position(self):
        """retrieves the value of the private attribute, position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the value of position

        Args:
            size(int): the value of position
        """
        if not type(position) == tuple and len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif not all(isinstance(x, int) for x in position):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = position
