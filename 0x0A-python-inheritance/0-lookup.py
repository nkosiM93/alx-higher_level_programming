#!/usr/bin/python3
"""Defines a function that returns a retuns
    the list of available attributes and methods
    of an object"""


def lookup(obj):
    """Returns the list of available attributes and
        methods in an object"""

    return dir(obj)
