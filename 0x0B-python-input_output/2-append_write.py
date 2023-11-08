#!/usr/bin/python3
"""
Module

a function that appends a string at the end of a text file (UTF8) and returns
the number of characters added
"""


def append_write(filename="", text=""):
    """
    Returns the number of characters written to a file
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        written = file.write(text)
    return (written)
