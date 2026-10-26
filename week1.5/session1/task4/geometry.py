# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

# Copy Point class definition here
class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__(self, x_coordinate, y_coordinate):
        """
        Creates a Point, given x & y coordinates.
        """
        self.x = x_coordinate
        self.y = y_coordinate
    # Add distance() method here

    def distance(self):
        """
        Returns distance from this Point to origin.
        """
        return math.hypot(self.x, self.y)
    # Add distance_to() method here 
    # (This will need a parameter representing another point)

    def distance_to(self, other_x, other_y):
        """
        Returns distance from this Point to another Point.
        """
        if self.x > other_x:
            x_diff = self.x - other_x
        elif self.x < other_x:
            x_diff = other_x - self.x
        else:
            x_diff = 0
        
        if self.y > other_y:
            y_diff = self.y - other_y
        elif self.y < other_y:
            y_diff = other_y - self.y
        else:
            y_diff = 0
        return math.hypot(x_diff, y_diff)
# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle
class Circle:

    def __init__(self, centre_point_object, radius):
        self.center = centre_point_object
        self.radius = radius

    def area(self):
        return (3.14 * (self.radius ** 2))
    
    def perimeter(self):
        return (3.14 * self.radius * 2)

origin = Point(0,0)
circle1 = Circle(origin, 25)
print(circle1.area())
print(circle1.perimeter())
# Don't add any testing code to this file!
