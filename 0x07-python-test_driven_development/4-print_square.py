#!/usr/bin/python3
"""
    Module contains a function that prints a square using the '#' symbol
"""


def print_square(size):
    """ Function prints the sqaure of size using the # symbola"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print("")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print("")
