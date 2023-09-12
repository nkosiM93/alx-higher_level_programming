#!/usr/bin/python3
"""Module contains a function that returns all the attributes of an object"""


def lookup(obj):
    """Function returns all attributes of obj"""

    if obj:
        return dir(obj)
    else:
        return []
