# import math
import math as m

############
# Question 2
############
print ("Question 2 - Calculate triangle angles from three coordinates")

# collect inputs of coordinates
x1, y1 = eval(input("Input first point (x, y): "))
x2, y2 = eval(input("Input second point (x, y): "))
x3, y3 = eval(input("Input third point (x, y): "))

# calculate the sides
a = m.sqrt((abs(x1 - x2)**2) + (abs(y1 - y2)**2))
b = m.sqrt((abs(x2 - x3)**2) + (abs(y2 - y3)**2))
c = m.sqrt((abs(x1 - x3)**2) + (abs(y1 - y3)**2))

# calculate the angles
A = m.degrees(m.acos((a**2 - b**2 - c**2) / (-2 * b * c)))
B = m.degrees(m.acos((b**2 - a**2 - c**2) / (-2 * a * c)))
C = m.degrees(m.acos((c**2 - b**2 - a**2) / (-2 * a * b)))

# display results
print(f"\nThe angles are {round(A*100)/100}, {round(B*100)/100}, {round(C*100)/100}")