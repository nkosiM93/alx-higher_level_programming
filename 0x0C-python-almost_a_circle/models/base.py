#!/usr/bin/python3
"""Module contains a base class"""
import json


class Base:
    """Base class for all other classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts object to JSON format"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):

        if len(list_objs) == 0 or list_objs is None:
            with open(f"{cls.__name__}.json", 'w') as myFile:
                myFile.write(Base.to_json_string([]))
        else:
            objDicts = []
            for inst in list_objs:
                objDicts.append(inst.to_dictionary())
            try:
                with open(f"{cls.__name__}.json", 'w') as myFile:
                    myFile.write(Base.to_json_string(objDicts))
            except Exception as e:
                print(f"{e}")
