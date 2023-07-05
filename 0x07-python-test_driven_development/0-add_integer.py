#!/usr/bin/python3
"""Module houses a function that adds two numbers"""


def add_integer(a, b=98):
    """Adds a to b and returns the result
        
        Args:
            a(int): first number
            b(int): second number

        Returns:
            int: the result of adding a and b
    """

    if not isinstance(a, (int, float)): 
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b

