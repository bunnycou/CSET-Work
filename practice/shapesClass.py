# Shapes but with classes
# X, Y, Size, Color
# loops for shapes instead of circle

# import and setup turtle
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

# show turtle, not required
turtle.showturtle()

class triangle:
    def __init__(self, x = 0, y = 0, size = 100, color = "black"):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.seth(0)
        turtle.color(self.color)
        turtle.begin_fill()

        for x in range(0, 3):
            turtle.forward(self.size)
            turtle.right(120)

        turtle.end_fill()

class square:
    def __init__(self, x = 0, y = 0, size = 100, color = "black"):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        
    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.seth(0)
        turtle.color(self.color)
        turtle.begin_fill()

        for x in range(0, 3):
            turtle.forward(self.size)
            turtle.right(90)

        turtle.end_fill()

class pentagon:
    def __init__(self, x = 0, y = 0, size = 100, color = "black"):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        
    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.seth(0)
        turtle.color(self.color)
        turtle.begin_fill()

        for x in range(0, 5):
            turtle.forward(self.size)
            turtle.right(72)

        turtle.end_fill()

triangle = triangle()
triangle.draw()

square = square(110, 0, 120, "red")
square.draw()

pentagon = pentagon(0, 110, 69, "blue")
pentagon.draw()

screen.exitonclick()