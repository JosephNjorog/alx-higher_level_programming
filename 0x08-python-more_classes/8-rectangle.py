#!/usr/bin/python3
"""Define a rectangle"""


class Rectangle:
    """Represents rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
            Checking for TypeError and ValueError
            then setting up the private var
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
            Checking for TypeError and ValueError
            then setting up the private var
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """
            Calculates the area of a rectangle
        """
        return self.height * self.width

    def perimeter(self):
        """
            Calculates the perimeter of a rectangle
        """
        if self.height == 0 or self.width == 0:
            return 0

        return (self.height + self.width) * 2

    def __str__(self):
        '''
            returning the string representation of the rectangle
        '''
        symbol = str(self.print_symbol)
        rectangle = ""
        if self.height == 0 or self.width == 0:
            return rectangle

        for h in range(self.height - 1):
            rectangle += symbol * self.width + "\n"
        rectangle += symbol * self.width
        return rectangle

    def __repr__(self):
        '''
            creating a recreation of the instance call
        '''
        rep = "{}({}, {})".format(self.__class__.__name__,
                                  self.width, self.height)
        return rep

    def __del__(self):
        '''
            printing a message with instance is deleted
        '''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''
            Checks if the rectangles are bigger or equal.
            Returns: The biggest rectangle or rect_1 if they are equal.
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        elif rect_1.area() >= rect_2.area():
            return rect_1
