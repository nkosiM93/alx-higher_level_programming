#!/usr/bin/python3
"""Modules for printing a square using #"""


def print_square(size):
    """Prints the square of a number using '#'
        
        Args:
            size(int): The number whose square must be printed
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

