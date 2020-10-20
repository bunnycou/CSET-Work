##############
# Question 2 #
##############
# Closest pair but with a GUI

import NearestPoints
from tkinter import Tk, Canvas

RADIUS = 2

class pairs:
    def __init__(self):
        self.points = list()

        # create window
        window = Tk()
        window.title("Closest Pairs")

        # create canvas
        self.canvas = Canvas(window, width = 400, height = 200)
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.addPoint)

        # stay open
        window.mainloop()

    def addPoint(self, event):
        if not self.isTooCloseToOtherPoints(event.x, event.y):
            self.addThisPoint(event.x, event.y)

    def addThisPoint(self, x, y):
        #display this point
        self.canvas.create_oval(x - RADIUS, y - RADIUS, x + RADIUS, y + RADIUS)

        # add that point to self.point list
        self.points.append([x, y])
        if len(self.points) > 2:
            p1, p2 = NearestPoints.nearestPoints(self.points)
            self.canvas.delete("line")
            self.canvas.create_line(self.points[p1][0], self.points[p1][1], self.points[p2][0], self.points[p2][1], tags="line")

    def isTooCloseToOtherPoints(self, x, y):
        for x in range(len(self.points)):
            if NearestPoints.distance(x, y, self.points[x][0], self.points[x][1]) <= RADIUS + 2:
                return True

pairs()