#!/usr/bin/python3
"""Module contains a class that inherits from the list class"""


class MyList(list):
    """Class inherits from list has a method that
        prints a sorted list in ascending order."""

    def print_sorted(self):
        """Prints out a sorteed list in ascending order"""

        newList = []

        for i in self:
            newList.append(i)
        newList.sort()
        print(newList)
