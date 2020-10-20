##############
# Question 1 #
##############
# Module
# Find the closest pair of coordinates

# calculate distance
def distance(x1, y1, x2, y2):
    # sqrt of a^2 + b^2
    return((x2-x1) * (x2-x1) + (y2-y1) * (y2-y1)) ** 0.5

# get nearest points from the list
def nearestPoints(points):
    # setup default
    p1, p2 = 0, 1
    shortestDistance = distance(points[p1][0], points[p1][1], points[p2][0], points[p2][1])

    # iterate through all points
    for x in range(len(points)):
        for y in range(x + 1, len(points)):
            d = distance(points[x][0], points[x][1], points[y][0], points[y][1])

            if d < shortestDistance:
                p1, p2 = x, y
                shortestDistance = d

    # send back results
    return p1, p2
