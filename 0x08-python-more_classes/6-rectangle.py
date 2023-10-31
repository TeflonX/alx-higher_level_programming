#!/usr/bin/python3
"""
Define class, Rectangle with private attribute width and height
"""


class Rectangle:
    """
    A class that defines the dimension of a rectangle
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes the variable, height and width needed to calculate
        the square of a rectangle

        Attr:
            width(int): width of the rectangle
            height(int): height of the rectangle
        """
        self.__width = width
        self.__height = height

        Rectangle.number_of_instances += 1

        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')

    @property
    def width(self):
        """
        return the private intance attribute, width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the value of a private instance attribute, width

        Attr:
            value(int): width of the rectangle
        """
        if type(self.__width) is not int:
            raise TypeError('width must be an integer')
        elif self.__width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """
        return the private intance attribute, height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the value of a private instance attribute, height

        Attr:
            height(int): height of the attribute
        """
        if type(self.__height) is not int:
            raise TypeError('height must be an integer')
        elif self.__height < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """
        returns the area of a rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        return the perimeter of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """
        returns the string representation of the rectangle
        """
        string = ''
        if self.__width == 0 or self.__height == 0:
            return string
        else:
            for i in range(self.__height):
                string += '#' * self.__width
                if i < self.__height - 1:
                    string += '\n'
            return string

    def __repr__(self):
        """
        return a string literal of the rectangle
        """
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """
        deletes the instance of a class and prints a message
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
