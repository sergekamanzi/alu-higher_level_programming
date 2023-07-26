#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = _import_('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def _init_(self, width, height):
        """Intialize a new Rectangle.

        :param width: The width of the new Rectangle.
        :type int:
        :param height: The height of the new Rectangle.
        :type int:
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the print() and str() reprentation """
        return self._width * self._height

    def _str_(self):
        """Return a description of the rectangle."""
        string = "[" + str(self._class.name_) + "] "
        string += str(self._width) + "/" + str(self._height)
        return string
