#!/usr/bin/python3
"""Module with func for appending data to a file"""


def append_write(filename="", text=""):
    """Appends data to the end of a file"""

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
