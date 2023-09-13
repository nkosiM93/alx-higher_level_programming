#!/usr/bin/python3
"""Module contains a class that calculates the area of a sqaure"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Class has methods that calculate the area of a square"""

    def __init__(self, size):
        # super().__init__(size, size)
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns the the area of a square"""

        return self.__size ** 2

    def __str__(self):
        return f"[{self.__class__.__name__}] {self.__size}/{self.__size}"
