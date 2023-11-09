#!/usr/bin/python3
"""
A funciton that returns the object to a text file
"""


def save_to_json_file(my_obj, filename):
    """
    reads a text file and returns the JSON object of the content of
    the file
    """
    import json

    with open(filename, mode='w', encoding="utf-8") as file:
        read_file = file.write(json.dumps(my_obj))
