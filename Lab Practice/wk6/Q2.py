##############
# Question 2 #
##############
# use classes and instances

from Q2_2 import circle

def main():
    circle1 = circle(1)
    circle2 = circle(25)
    circle3 = circle(125)

    print(f"Circle with radius {circle1.radius} has an area of {circle1.getArea()}")
    print(f"Circle with radius {circle2.radius} has an area of {circle2.getArea()}")
    print(f"Circle with radius {circle3.radius} has an area of {circle3.getArea()}")

    circle2.radius = 100

    print(f"Circle with modified radius {circle2.radius} has an area of {circle2.getArea()}")

main()