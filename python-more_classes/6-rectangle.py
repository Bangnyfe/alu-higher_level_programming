#!/usr/bin/python3
"""
This module defines the Rectangle class.

The Rectangle class allows creation of rectangle objects with width and height.
It includes methods to calculate area, perimeter, and string representations.
It also tracks the number of active Rectangle instances.
"""


class Rectangle:
    """Defines a rectangle by width and height, and tracks instances."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize rectangle with width and height (default is 0)."""
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
        """Return string representation of the rectangle using '#' characters."""
        if self.width == 0 or self.height == 0:
            return ""
        row = "#" * self.width
        return "\n".join([row for _ in range(self.height)])

    def __repr__(self):
        """Return string that recreates the rectangle using eval()."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print message and update instance count on deletion."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
