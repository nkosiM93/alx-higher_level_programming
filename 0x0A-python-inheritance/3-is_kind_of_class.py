#!/usr/bin/python3
"""Modulecontains a function that checks if an object is an insatnce of a
    certain given class"""


def is_kind_of_class(obj, a_class):
    """Returns true if obj is an insatnce of a_class or a class derived from
    the said class"""

    if isinstance(obj, a_class):
        return True
    else:
        return False
