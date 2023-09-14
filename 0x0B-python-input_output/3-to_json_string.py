#!/usr/bin/python3
"""Module contains funct that encodes in JSON"""
import json


def to_json_string(my_obj):
    """Encodes my_obj in JSON Fomrat"""

    return json.dumps(my_obj)
