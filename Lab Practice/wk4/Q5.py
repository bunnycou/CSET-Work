############
# Question 5
############
# Detecting the location of an object in a circle with turtle.
# import and set turtle
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

# get user inputs
x1, y1 = eval(input("Enter the center of the circle x, y: "))
radius = eval(input("Enter the radius of the circle: "))
x2, y2 = eval(input("Enter a point x, y: "))

# compute distance
d = ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) ** 0.5

# turtle properties
turtle.showturtle()

# draw circle and point
turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.circle(radius)
turtle.penup()
turtle.goto(x2, y2)
turtle.pendown()
turtle.dot(6, "red")

# display status
turtle.penup()
turtle.goto(x1 - 70, y1 - radius - 20)
turtle.pendown()

if d <= radius:
    turtle.write("The point is inside the circle")
else:
    turtle.write("The point is outside the circle")

turtle.hideturtle()

# wait for the user to click to exit
screen.exitonclick()