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
