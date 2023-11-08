#!/usr/bin/python3
import json
"""
a function that returns the JSON representation of an object (string)
"""


def to_json_string(my_obj):
    """
    Returns json.dump(my_obj)
    """
    return json.dumps(my_obj)
