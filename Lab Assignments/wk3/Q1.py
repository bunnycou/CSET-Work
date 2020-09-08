# Noah Cousino
# R01506332

# import maths
from math import sqrt, sin, pi

# collect radius
radi = eval(input("Enter the radius of the pentagon (such as 5.5): "))

# calculate side and area
s = (2 * radi) * sin(pi/5)
a = ((3 * sqrt(3))/2) * s**2

# display area
print(f"The area of the pentagon is {round(a, 2)}")
