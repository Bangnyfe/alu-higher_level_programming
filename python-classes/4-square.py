#!/usr/bin/python3
"""Defines a class Square with size property and area computation."""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size=0):
        """
        Initializes the square with a given size.

        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size  # Use the setter for validation

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): The size value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
