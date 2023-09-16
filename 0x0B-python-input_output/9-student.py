#!/usr/bin/python3
"""Module has a funct that prints a JSON repr of an object"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """To json repre"""

        return self.__dict__
