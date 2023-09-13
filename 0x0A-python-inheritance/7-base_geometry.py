#!/usr/bin/python3
"""Module contains a geometry class"""


class BaseGeometry:
    """Class containing methods and functions that do some geometry"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value argument whether it's an integer or not"""

        if type(value) is not int:
            raise TypeError(f"{name:s} must be an integer")
        if value <= 0:
            raise ValueError(f"{name:s} must be greater than 0")
