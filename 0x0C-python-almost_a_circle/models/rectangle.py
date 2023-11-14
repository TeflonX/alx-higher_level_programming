#!/usr/bin/python3
"""
A retangle class
"""


from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the attributes of a class
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        retrieves value for the width of the rectangle

        Returns:
            self.__width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        assigns value to the width of a private instance attribute

        Args:
            width = width of the rectangle
        """
        self.__width = width

    @property
    def height(self):
        """
        returns for the height of the rectangle

        Returns:
            self.__height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        asssigns value private instance atribute, height

        Args:
            height = height of the rectangle
        """
        self.__height = height

    @property
    def x(self):
        """
        retrieves the value for an instance attribute, x

        Returns:
            self.__x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        assigns value to the private instance attribute, x

        Args:
            x
        """
        self.__x = x

    @property
    def y(self):
        """
        retrieves the value to a private instance attribute, y

        Returns:
            self.__y
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        assigns value to a private instance attribute, y

        Args:
            y
        """
        self.__y = y
