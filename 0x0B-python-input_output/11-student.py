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

    def reload_from_json(self, json=None):
        for k, v in json.items():
            if k in self.__dict__:
                self.__dict__[k] = v
