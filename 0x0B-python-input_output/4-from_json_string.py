#!/usr/bin/python3
"""Contains a function that returns a JSON repr of a Python Object"""
import json


def from_json_string(my_str):
    """Returns a JSON repr of a Python Object"""

    return json.loads(my_str)
