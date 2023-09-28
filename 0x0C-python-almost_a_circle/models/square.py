#!/usr/bin/python3
"""Module contains a Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Models a square and inherits from the Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return (f"[{self.__class__.__name__}] ({self.id}) "
                f"{self.x}/{self.y} - {self.size}")

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates object attributes"""
        list_attr = ['id', 'size', 'x', 'y']
        if args is not None and not len(args) == 0:
            for a in range(len(args)):
                setattr(self, list_attr[a], args[a])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)
