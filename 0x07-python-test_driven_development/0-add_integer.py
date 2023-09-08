#!/usr/bin/python3
""" Module contains a function that adds two numbers """


def add_integer(a, b=98):
    """ Adds two integers

        Args:
            a (int): 1st integer
            b (int): 2nd integer

        """

    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
