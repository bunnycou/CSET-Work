##############
# Question 2 #
##############
# second file for Q2

#import maths
from math import pi

class circle:
    def __init__(self, radius):
        self.radius = radius

    def getPerimeter(self):
        return 2 * pi * self.radius
    
    def getArea(self):
        return pi * (self.radius**2)
    
    def getRadius(self, radius):
        self.radius == radius