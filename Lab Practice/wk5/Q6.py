##############
# Question 6 #
##############
# default argument practice

def printArea(width = 1, height = 2):
    area = width * height
    print(f"\nWidth: {width}\nHeight: {height}\nArea: {area}")

printArea()
printArea(4, 2.5)
printArea(height = 5, width = 3)
printArea(width = 1.2)
printArea(height = 6.2)