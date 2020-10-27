# superclass

class GeometricObject:
    def __init__(self, color = "green", filled = True):
        self.__color = color
        self.__filled = filled

    def getColor(self):
        return self.__color
    def setColor(self, color):
        self.__color = color

    def isFilled(self):
        return self.__filled
    def setFilled(self, filled):
        self.__filled = filled

    # provides string description for object: str(GeometricObject())
    def __str__(self):
        return f"color: {self.__color} and filled: {str(self.__filled)}"