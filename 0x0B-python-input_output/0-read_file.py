#!/usr/bin/python3
"""Module contains a func that reads from a text file"""


def read_file(filename=""):
    """Function reads from a tetx file"""

    with open(filename, encoding="utf-8") as myFile:
        for line in myFile:
            print(f"{line}", end="")
