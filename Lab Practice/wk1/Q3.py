# import and set turtle
from turtle import Turtle, Screen
turtle = Turtle()
screen = Screen()

############
# Question 3
############

print("Question 3 - Draw four squares in turtle")

# draw the turtle four square
turtle.showturtle()

#drawing squares like
# 4 1
# 3 2
# draw squares
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)

turtle.forward(200)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

# leaves turtle open until clicked
screen.exitonclick()