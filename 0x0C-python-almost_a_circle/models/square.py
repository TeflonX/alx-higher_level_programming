#!/usr/bin/python3
"""
A Square class that inherits from the rectangle class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initializes the attributes of the class with the base class
        attribute

        Attr:
            size: width or height of rectangle
            x: int
            y: int
            id: int
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns the string representation of a square
        """
        return (f"[Square] ({self.id}) {self.x}/"
                f"{self.y} - {self.width}")

    @property
    def size(self):
        """
        Returns the dimension of a square
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        sets the value of size

        Args:
            size: dimension of a square
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        Sets the value of attributes using args and kwargs
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            self.id = kwargs.get('id', self.id)
            self.size = kwargs.get('size', self.size)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)

    def to_dictionary(self):
        """
        Returns a dictionary representation of a square
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
