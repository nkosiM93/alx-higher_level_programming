#!/usr/bin/python3
"""Module has a funct that prints a JSON repr of an object"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """To json repre"""

        f_dict = {}
        if isinstance(attrs, list) and \
                all(isinstance(x, str) for x in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
