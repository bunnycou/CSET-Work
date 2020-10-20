##############
# Question 1 #
##############
# Test file for nearestpoints

import NearestPoints

def main():
    numberOfPoints = eval(input("Eneter the number of coordinates: "))

    # create a list to store points
    points  = list()

    print(f"Enter {numberOfPoints} points")
    # collect all inputs
    for _ in range(0, numberOfPoints):
        point = 2* [0]
        point[0], point[1] = eval(input("Enter coordinates seperated by comma: "))
        points.append(point)

    # get the two nearest
    p1, p2 = NearestPoints.nearestPoints(points)

    # display results
    print(f"The closest two points are ({str(points[p1][0])}, {str(points[p1][1])}) and ({str(points[p2][0])}, {str(points[p2][1])})")

main()