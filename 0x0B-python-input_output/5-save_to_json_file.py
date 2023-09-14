#!/usr/bin/python3
"""Module: Funct saves JSON Obj to file"""
import json


def save_to_json_file(my_obj, filename):
    """Saves json encoding to file"""

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
