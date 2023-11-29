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
        if self.id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        import json
        """
        that returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
