#!/usr/bin/python3
"""
a function that returns an object (Python data structure) represented by
a JSON string
"""


def from_json_string(my_str):
    """
    decodes a JSON string
    """
    import json
    return json.loads(my_str)
