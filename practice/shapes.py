# Shape Functions
# Triangle Square Pentagon
# X, Y, Size, Color
# loops for shapes instead of circle

# import and setup turtle
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

# show turtle, not required
turtle.showturtle()

# functions for making the shapes
def triangle(x = 0, y = 0, size = 100, color = "black"):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.seth(0)
    turtle.color(color)
    turtle.begin_fill()

    for x in range(0, 3):
        turtle.forward(size)
        turtle.right(120)

    turtle.end_fill()

def square(x = 0, y = 0, size = 100, color = "black"):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.seth(0)
    turtle.color(color)
    turtle.begin_fill()

    for x in range(0, 4):
        turtle.forward(size)
        turtle.right(90)

    turtle.end_fill()

def pentagon(x = 0, y = 0, size = 100, color = "black"):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.seth(0)
    turtle.color(color)
    turtle.begin_fill()

    for x in range(0, 5):
        turtle.forward(size)
        turtle.right(72)

    turtle.end_fill()

# call functions
triangle(0, 0, 100, "black")
square(110, 0, 120, "red")
pentagon(0, 110, 69, "blue")

# keep turtle open and hide it
turtle.hideturtle()
screen.exitonclick()