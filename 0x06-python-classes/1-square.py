#!/usr/bin/python3
"""Defines a class named Square"""


class Square:
    """calculates the area of a square and prints it"""
    def __init__(self, size=0):
        """initializes the size of the square

        Args:
            size(int): size of the square
        """
        self.__size = size
