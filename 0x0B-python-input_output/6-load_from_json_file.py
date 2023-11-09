#!/usr/bin/python3
"""
A function that creates an object from a JSON file
"""


def load_from_json_file(filename):
    """
    decode a JSON object content of a text file
    """
    import json

    with open(filename, encoding="utf-8") as file:
        return json.loads(file.read())
