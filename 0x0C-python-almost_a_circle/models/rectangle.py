#!/usr/bin/python3
"""Contains a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle modelling class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes instances """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Gets width"""
        
        return self.__width

    @width.setter
    def width(self, w):
        """Sets width"""
        
        self.__width = w

    @property
    def height(self):
        """Gets width"""
        
        return self.__height

    @height.setter
    def height(self, h):
        """Sets width"""
        
        self.__height = h

    @property
    def x(self):
        """ Sets width"""
        
        return self.__x

    @x.setter
    def x(self, x):
        """ Sets width"""
        
        self.__x = x

    @property
    def y(self):
        """ Sets width"""

        return self.__y

    @y.setter
    def y(self, y):
        """ Sets width"""

        self.__y = y
