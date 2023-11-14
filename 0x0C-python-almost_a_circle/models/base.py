#!/usr/bin/python3
"""
The base class of every other classes in this project
"""


class Base:
    """
    A class named Base
    """

    __nb_objects = 0
    def __init__(self, id=None):
        """
        Initializes the instance of a variable
        """
        self.id = id
        if self.id == None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
