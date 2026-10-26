# Week 1.5, Session 1: Task 3
import math



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

    def distance(self):
        """
        Returns distance from this Point to origin.
        """
        return math.hypot(self.x, self.y)
    
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

    # Add distance() method here

    # Add distance_to() method here
    # (This will need a parameter representing another point)



# Finally, add code here to demonstrate use of Point
