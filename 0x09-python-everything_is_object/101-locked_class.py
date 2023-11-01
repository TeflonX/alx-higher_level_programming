#!/usr/bin/python3
"""
a class named LockedClass
"""


class LockedClass:
    """
    a class that that prevents the user from dynamically creating new
    instance attributes
    """
    __slots__ = ['first_name']
