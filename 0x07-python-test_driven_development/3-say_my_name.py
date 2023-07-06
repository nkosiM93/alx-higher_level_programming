#!/usr/bin/python3
"""Module houses a function stores and prints
    some strings"""


def say_my_name(first_name, last_name=""):
    """Prints name and surname.

        Args:
            first_name(str):First name
            last_names(str):Last name
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {} ".format(first_name, last_name))
