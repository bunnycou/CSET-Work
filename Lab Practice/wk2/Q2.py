# get pi
from  math import pi

############
# Question 2
############
print("Question 2 - Read radius and length input and output area and volume of a cylinder\n")

rad = eval(input("Input radius of a cylinder: "))
len = eval(input("Input length of a cylinder: "))

area = (rad**2) * pi
vol = area * len

print(f"\nThe area is {round(area, 2)}\nThe volume is {round(vol, 2)}")