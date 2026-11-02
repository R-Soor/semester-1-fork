# Week 1.6, Session 1: Task 3

import math
from point import Point

VALID_COLOURS = {"red", "orange", "yellow", "green", "blue", "purple"}


class Shape:
    """
    Superclass for different types of shape.
    """

    def __init__(self, position, colour):
        """
        Creates a shape with the specified position & colour.
        """
        self.set_position(position)
        self.set_colour(colour)

    def set_position(self, position):
        """
        Moves this shape to the given position.
        """
        if not isinstance(position, Point):
            raise TypeError("position must be a Point")

        self.position = position

    def set_colour(self, colour):
        """
        Sets this shape's colour to the given colour.
        """
        if colour not in VALID_COLOURS:
            raise ValueError(f"invalid color: must be one of {VALID_COLOURS}")

        self.colour = colour

class Circle(Shape):
    def __init__(self, radius, position, colour="red"):
        super().__init__(position,colour)
        self.colour=colour
        self.position=position
        self.radius=self.set_radius(radius)

    def set_radius(self,r):
        if not isinstance(r, (int, float)):
            raise TypeError("Radius needs to be integer or float")
        elif r<0:
            raise ValueError("Radius needs to be greater than 0")
        else:
            return r
    
        
    def __str__(self):
        return f"{self.colour} circle, radius {self.radius}, at {str(self.position)}"
    
    def area(self):
        return round((math.pi*(self.radius**2)),3)
    
    def perimeter(self):
        return round((math.pi*2*self.radius),3)

    def change_position(self, x, y):
        print("Moving the circle")
        self.position=self.set_position(Point(x,y))

    def change_colour(self, colour):
        print("Changing the Circle's colour")
        self.set_colour(colour)

