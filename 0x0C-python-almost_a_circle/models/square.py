#!/usr/bin/python3
"""Module contains a Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Models a square and inherits from the Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self):
        return (f"[{self.__class__.__name__}] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}/{self.height} "
                f"- {self.width}")
