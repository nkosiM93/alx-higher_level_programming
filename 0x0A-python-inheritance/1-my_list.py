#!/usr/bin/python3
"""Defines a class that inherits from list"""


class MyList(list):
    """defines a list of integers"""

    def print_sorted(self):
        """Prints the list but sorted"""
        # print(sorted(self))
        return sorted(self)
