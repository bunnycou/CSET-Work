# subclass
from GeometricObject import GeometricObject
from math import pi

class Circle(GeometricObject):
    def __init__(self, radius = 10):
        super().__init__() # initialize geometric as super
        self.__radius = radius

    def getRadius(self):
        return self.__radius
    def setRadius(self, radius):
        self.__radius = radius

    def getArea(self):
        return self.__radius**2 * pi

    def getDiameter(self):
        return self.__radius * 2
    
    def getPerimeter(self):
        return 2 * pi * self.__radius

    def printCircle(self):
        print(f"{self.__str__()} radius: {str(self.__radius)}")
