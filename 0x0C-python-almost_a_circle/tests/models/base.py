#!/usr/bin/python3
"""Module contains a base class"""


class Base:
    """Base class for all other classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
