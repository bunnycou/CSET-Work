from CircleClass import Circle
from RectangleClass import Rectangle

def main():
    circle = Circle(1.5)
    print(f"A Circle {circle}")
    print(f"The Radius is: {circle.getRadius()}")
    print(f"The area is: {circle.getArea()}")
    print(f"The diameter is: {circle.getDiameter()}")

    rectangle = Rectangle(2, 4)
    print(f"A rectangle {rectangle}")
    print(f"The area is: {rectangle.getArea()}")
    print(f"The perimeter is {rectangle.getPerimeter()}")

main()