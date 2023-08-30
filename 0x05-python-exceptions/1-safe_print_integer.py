#!/usr/bin/python3

def safe_print_integer(value):

    result = False

    try:
        print("{:d}".format(value))
        result = True
        return result
    except (ValueError, TypeError):
        return result

