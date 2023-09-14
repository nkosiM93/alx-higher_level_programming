#!/usr/bin/python3
"""Module containts a function that adds an attr to a func if possible"""


def add_attribute(ob, name, val):
    """Adds an attr to an ob only if possible"""

    if not isinstance(ob, (int, float, complex, str, tuple, frozenset,
                           bool, None.__class__, bytes, bytes, bytearray,
                           type(None))):
        ob.name = val
    else:
        raise TypeError("can't add new attribute")
