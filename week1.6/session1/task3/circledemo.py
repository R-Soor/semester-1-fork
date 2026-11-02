# Week 1.6, Session 1: Task 3
from shapes import Circle, Shape, Point
# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)
p=Point(0,0)
c=Circle(2.5,p)
#    red circle, radius 2.5, at (0.0, 0.0)
#    Area = 19.635
#    Perimeter = 15.708
#    Moving the circle...
#    red circle, radius 2.5, at (1.6, 3.2)
#    Changing the circle's colour...
#    green circle, radius 2.5, at (1.6, 3.2)
print(str(c))
print(c.area())
print(c.perimeter())
