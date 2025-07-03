#!/usr/bin/python3
"""
This module defines the Rectangle class.

The Rectangle class provides a representation of a geometric rectangle.
It supports width and height validation, computing area and perimeter,
instance tracking, string and eval representations, customizable print
symbols, and comparison between rectangles based on area.
"""


class Rectangle:
    """Defines a rectangle with width, height, and print symbol."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize rectangle with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return

