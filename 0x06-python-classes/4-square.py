#!/usr/bin/python3
"""Creates a square"""


class Square:
    """Defines a Square"""

    def __init__(self, size=0):
        """Defines the dimensions of the square

        Args:
            size(int): The dimension of one side
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Gets/returns the size attribute"""
        return self.__size

    @size.setter
    def size(self, size=0):
        """Defines the dimensions of the square

        Args:
            size(int): The dimension of one side
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Method calculates and returns the area of a square"""
        return self.__size ** 2
