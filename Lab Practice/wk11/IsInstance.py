from CircleClass import Circle
from RectangleClass import Rectangle

def main():
    c = Circle(4)
    r = Rectangle(1, 3)
    print("Circle: ")
    displayObject(c)
    print("Rectangle: ")
    displayObject(r)

def displayObject(g):
    print(g.__str__())

    if isinstance(g, Circle):
        print(f"Diameter is {g.getDiameter()}")
    elif isinstance(g, Rectangle):
        print(f"Width is {g.getWidth()}")
        print(f"Height is {g.getHeight()}")

main()