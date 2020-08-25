from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

# print table
print("Print Table:")
print("a  a^2  a^3\n1  1  1\n2  4  8\n3  9  27\n4  16  64")

# small space
print("")

# calculate
print("Calculate Expression:")
print(((9.5 * 4.5) - (2.5 * 3)) / (45.5 - 3.5))

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