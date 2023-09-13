#!/usr/bin/python3
"""Contains a class that inverts the == and thr != operation"""


class MyInt(int):
    """Class inverts == and != functionality"""

    def __eq__(self, val):
        """Inversion happens here"""

        return not super().__eq__(val)

    def __ne__(self, val):
        """Inversion Happens Here"""

        return not super().__ne__(val)
