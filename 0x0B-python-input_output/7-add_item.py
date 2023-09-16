#!/usr/bin/python3
"""Load, add, save to a JSON File"""
import sys
import json
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file


myL = load_from_json_file("add_item.json")
def addToList():
    """Adds items to a list """

    if len(sys.argv) > 1:
        for i in range(len(sys.argv)):
            if i != 0:
                myL.append(sys.argv[i])

if __name__ == "__main__":
    addToList()
    save_to_json_file(myL, "add_item.json")
