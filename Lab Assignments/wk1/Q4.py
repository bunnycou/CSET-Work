# Noah Cousino
# R01506332

#import dependencies
from turtle import Turtle, Screen
from math import sqrt

turtle = Turtle()
screen = Screen()

# Display turtle
turtle.showturtle()

# using function to automate the connector lines
def conlin(x, y):
    turtle.up()
    turtle.setpos(x, y)
    turtle.down()
    turtle.seth(225)
    turtle.forward(sqrt(5000))

def drawbox(x, y):
    turtle.up()
    turtle.setpos(x, y)
    turtle.down()
    turtle.seth(0)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(150)

# draw cube
# draw the rectangles
drawbox(-200, 200)
drawbox(-250, 150)

# draw the rest of the connector lines
conlin(-200, 200)
conlin(100, 200)
conlin(100, 50)
conlin(-200, 50)

# hide turtle
turtle.ht()

# keep turtle onscreen
screen.exitonclick()