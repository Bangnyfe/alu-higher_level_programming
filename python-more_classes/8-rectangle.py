#!/usr/bin/python3
"""
This module defines the Rectangle class.

The Rectangle class defines a geometric rectangle using private width
and height attributes, and provides methods to compute area and perimeter.

Features:
- Instance counting via `number_of_instances`
- Customizable symbol for string representation via `print_symbol`
- A static method `bigger_or_equal` to compare two rectangles by area
- String and eval-compatible representations
- Input validation for all attributes
- Cleanup message on deletion
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
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle, or 0 if width or height is 0."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return the string representation using print_symbol."""
        if self.width == 0 or self.height == 0:
            return ""
        symbol = str(se
