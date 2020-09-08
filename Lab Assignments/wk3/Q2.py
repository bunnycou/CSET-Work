# Noah Cousino
# R01506332

# import and set turtle
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

# set universal turtle properties
turtle.pensize(5)

# create a function that draws the circle given coordinates and color
def circ(color, x, y) :
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.circle(50)

# draw the circles
# b, bk, r, y, gr
circ("blue", -90, 25)
circ("black", 0, 25)
circ("red", 90, 25)
# second row
circ("yellow", -45, -25)
circ("green", 45, -25)

# exit when user clicks
screen.exitonclick()
