# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width:int, height:int):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        if not isinstance(width,int):
            raise TypeError("Width must be an integer")
        elif width<=0:
            raise ValueError("Width must be greater than 0")
        if not isinstance(height,int):
            raise TypeError("Height must be an integer")
        elif height<=0:
            raise ValueError("Height must be greater than 0")
        
        self.width = width
        self.height = height

    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)
    def is_square(self):
        """
        Returns true if rectangle is a square
        """
        if self.height==self.width:
            return True
        else:
            return False
    def area(self):
        """
        Returns area of rectangle
        """
        return self.width*self.height
    def perimeter(self):
        """
        Returns perimeter of rectangle
        """
        return (2*self.width)+(2*self.height)