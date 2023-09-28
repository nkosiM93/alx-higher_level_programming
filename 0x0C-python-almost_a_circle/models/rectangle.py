#!/usr/bin/python3
"""Contains a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle modelling class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes instances """
        super().__init__(id)

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """Gets width"""
        return self.__width

    @width.setter
    def width(self, w):
        """Sets width"""
        if not isinstance(w, int):
            raise TypeError("width must be an integer")
        if w <= 0:
            raise ValueError("width must be > 0")
        self.__width = w

    @property
    def height(self):
        """Gets width"""
        return self.__height

    @height.setter
    def height(self, h):
        """Sets width"""
        if not isinstance(h, int):
            raise TypeError("height must be an integer")
        if h <= 0:
            raise ValueError("height must be > 0")
        self.__height = h

    @property
    def x(self):
        """ Sets width"""
        return self.__x

    @x.setter
    def x(self, x):
        """ Sets width"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ Sets width"""
        return self.__y

    @y.setter
    def y(self, y):
        """ Sets width"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints out a representation of the rectangle using # symbol"""
        for u in range(self.__y):
            print()
        for i in range(self.__height):
            print(f"{' ' * self.__x}", end="")
            for j in range(self.__width):
                print(f"#", end="")
            print()

    def __str__(self):
        return (f"[{self.__class__.__name__}] ({self.id}) "
                f"{self.__x}/{self.__y} - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """Updates the class attributes"""
        list_atr = ['id', 'width', 'height', 'x', 'y']
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Returns a dictionary representation of the object"""
        return vars(self)
