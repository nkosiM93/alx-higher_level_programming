#!/usr/bin/python3
"""Module contains a funtion that prints a paragraph"""


def text_indentation(text):
    """Function prints indented text"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(text[i])
            print("")
            if i + 1 < len(text):
                if text[i + 1] == " ":
                    i += 1
            i += 1
        else:
            print(text[i], end="")
            i += 1
