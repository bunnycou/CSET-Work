# get pi from the math module
from  math import pi

# Question 1
# Read celsius input and output fahrenheit
print("Question 1\n")

ce = eval(input("Input a degree in celsius: "))
fa = ((9/5) * ce) + 32

print(f"\n{ce} in celsius is {fa} in fahrenheit")

print("\n-----\n")

# Question 2
# Read radius and length input and output area and volume of a cylinder
print("Question 2\n")

rad = eval(input("Input radius of a cylinder: "))
len = eval(input("Input length of a cylinder: "))

area = (rad**2) * pi
vol = area * len

print(f"\nThe area is {round(area, 2)}\nThe colume is {round(vol, 2)}")

print("\n-----\n")

# Question 3
# Read feet and convert into meters
print("Question 3\n")

ft = eval(input("Input feet: "))
me = ft * 0.305

print(f"\n{ft} feet is {me} meters")

print("\n\n")