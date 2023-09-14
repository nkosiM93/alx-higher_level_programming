#!/usr/bin/python3
"""Module: Funct creates obj from JSON file"""
import json


def load_from_json_file(filename):
    """Creates obj from JSON file"""

    with open(filename, encoding="utf-8") as f:
        return json.load(f)
