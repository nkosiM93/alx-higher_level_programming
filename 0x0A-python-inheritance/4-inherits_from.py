#!/usr/bin/python3
"""Module contains a function that checks if an object is a subclass of a
    certain given class or a class that inherits from the specified class"""


def inherits_from(obj, a_class):
    """Returns true if obj is an insatnce of a_class or a class derived from
    a_class"""
    
    return False if type(obj) is a_class else isinstance(obj, a_class)
