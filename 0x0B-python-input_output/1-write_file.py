#!/usr/bin/python3
"""Module has func that writes to a file"""


def write_file(filename="", text=""):
    """Writes to a file, overwrites if file already has content"""

    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
