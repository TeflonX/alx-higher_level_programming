#!/usr/bin/python3
"""
Module

a function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    prints the lines in a text file
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        for line in file:
            print(line, end='')
