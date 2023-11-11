#!/usr/bin/python3
"""
a class Student that defines a student by Public instance attributes:
first_name, last_name and age
"""


class Student:
    """
    a class that defines individual students
    """
    def __init__(self, first_name, last_name, age):
        """
        initializes the attributes of class instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        retrieves a dictionary representation of a Student instance
        """
        return_dict = {}
        for key, value in self.__dict__.items():
            return_dict[key] = value

        return return_dict
