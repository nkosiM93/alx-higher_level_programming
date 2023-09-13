#!/usr/bin/python3
"""Modulecontains a function that checks if an object is an insatnce of a
    certain given class"""


def is_same_class(obj, a_class):
    """Returns true if obj is an exact insatnce of a_class"""

    if type(obj) == a_class:
        return True
    else:
        return False
