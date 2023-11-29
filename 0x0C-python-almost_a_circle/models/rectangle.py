#!/usr/bin/python3
"""
A retangle class
"""


from models.base import Base


class Rectangle(Base):
    """
    determines the size of a rectangle using its width and height.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the attributes of a class
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        else:
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
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        else:
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
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        else:
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
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = y

    def area(self):
        """
        Calculates the area of the square and returns the value
        """
        return self.__width * self.__height

    def display(self):
        """
        prints the square
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def update(self, *args, **kwargs):
        """
        A public method that assigns an argument to each attribute

        Args:
            *args:
                magic variable
            *kwargs:
                magic variable
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif kwargs:
            self.id = kwargs.get('id', self.id)
            self.width = kwargs.get('width', self.width)
            self.height = kwargs.get('height', self.height)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)


    def __str__(self):
        """
        return string representation of the rectangle
        """
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}/{self.height}")
