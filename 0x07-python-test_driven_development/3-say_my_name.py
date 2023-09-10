#!/usr/bin/python3
""" Module contains a function that prints out
    text"""


def say_my_name(first_name, last_name=""):
    """ Function prints user name and surname

        Args:
            first_name (string): NAme of the user
            last_name (String): User's last name
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name:s} {last_name:s}")
