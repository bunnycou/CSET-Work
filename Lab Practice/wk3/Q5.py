############
# Question 5
############
# import and set turtle
from turtle import Turtle, Screen
turtle = Turtle()
screen = Screen()

# show turtle
turtle.showturtle()

# set turtle properties
turtle.pensize(3)
turtle.penup()
turtle.goto(-200, -50)
turtle.pendown()

# draw triangle
turtle.begin_fill()
turtle.color("red")
turtle.circle(40, steps = 3)
turtle.end_fill()

turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()

# draw square
turtle.begin_fill()
turtle.color("blue")
turtle.circle(40, steps = 4)
turtle.end_fill()

turtle.penup()
turtle.goto(0, -50)
turtle.pendown()

# draw pentagon
turtle.begin_fill()
turtle.color("green")
turtle.circle(40, steps = 5)
turtle.end_fill()

turtle.penup()
turtle.goto(100, -50)
turtle.pendown()

#draw hexagon
turtle.begin_fill()
turtle.color("yellow")
turtle.circle(40, steps = 6)
turtle.end_fill()

turtle.penup()
turtle.goto(200, -50)
turtle.pendown()

#draw circle
turtle.begin_fill()
turtle.color("red")
turtle.circle(40)
turtle.end_fill()

turtle.color("green")
turtle.penup()
turtle.goto(-100, 50)
turtle.pendown()

turtle.write("Colors and Shapes", font = ("Times", 18, "bold"))

turtle.hideturtle()

# close turtle when clickeds
screen.exitonclick()