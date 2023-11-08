#!/usr/bin/python3
"""
Module

a function that writes a string to a text file (UTF8) and returns the
number of characters written
"""


def write_file(filename="", text=""):
    """
    Returns number of lines in a text file
    """
    with open(filename, "w", encoding='utf-8') as file:
        written = file.write(text)
    return (written)
