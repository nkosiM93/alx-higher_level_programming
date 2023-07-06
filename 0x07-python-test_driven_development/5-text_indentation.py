#!/usr/bin/python3
"""String editor module"""


def text_indentation(text):
    """Ëdits a string and breaks it"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    c = 0

    while c < len(text):
        if text[c] != "." and text[c] != "?" and text[c] != ":":
            print("{}".format(text[c]), end="")
            c += 1
        else:
            print("{}".format(text[c]), end="")
            if not (c + 1 >= len(text)):
                if text[c + 1] == " ":
                    c += 1
            print()
            print()
            c += 1
