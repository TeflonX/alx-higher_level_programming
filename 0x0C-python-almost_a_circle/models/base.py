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

    @classmethod
    def save_to_file(cls, list_objs):
        import sys
        """
        A class method that writes the JSON string representation of list_objs
        to a file:
        """
        dict_list = []
        if list_objs is None:
            list_objs = dict_list

        if list_objs is not None:
            for obj in list_objs:
                dict_list.append(cls.to_dictionary(obj))

            file_name = f"{cls.__name__}.json"

            with open(file_name, "w") as file:
                json_str = cls.to_json_string(dict_list)
                file.write(json_str)
