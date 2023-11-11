#!/usr/bin/python3
"""
a function that returns the dictionary description with simple data structure
(list, dictionary, string, integer and boolean) for JSON serialization of an
object
"""


def class_to_json(obj):
    """Converts an object's attributes to a JSON-serializable dictionary."""
    json_data = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_data[key] = value

    return json_data
