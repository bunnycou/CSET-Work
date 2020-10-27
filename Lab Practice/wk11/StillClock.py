from math import pi, sin, cos
from datetime import datetime
from tkinter import Canvas

class StillClock(Canvas):
    def __init__(self, container):
        super().__init__(container)
        self.setCurrentTime()

    def getHour(self):
        return self.__hour
    def setHour(self, hour):
        self.__hour = hour
        self.delete("clock")
        self.drawClock()
    
    def getMinute(self):
        return self.__minute
    def setMinute(self, minute):
        self.__minute = minute
        self.delete("clock")
        self.drawClock()

    def getSecond(self):
        return self.__second
    def setSecond(self, second):
        self.__second = second
        self.delete("clock")
        self.drawClock()

    def setCurrentTime(self):
        d = datetime.now()
        self.__hour = d.hour
        self.__minute = d.minute
        self.__second  = d.second
        self.delete("clock")
        self.drawClock()

    def drawClock(self):
        width = float(self["width"])
        height = float(self["height"])
        radius  = min(width , height)/2.4

        secondHandLength = radius * 0.8
        minuteHandLength = radius * 0.66
        hourHandLength = radius * 0.5

        self.create_oval(width / 2 - radius, height / 2 - radius, width/2 + radius, height / 2 + radius, tags = "clock")
        self.create_text(width / 2 - radius + 5, height / 2, text = "9", tags = "clock")
        self.create_text(width / 2 + radius - 5, height / 2, text = "3", tags = "clock")
        self.create_text(width / 2, height / 2 - radius + 5, text = "12", tags = "clock")
        self.create_text(width / 2, height / 2 + radius - 5, text = "6", tags = "clock")

        xCenter = width / 2
        yCenter = height / 2

        second = self.__second
        xSecond = xCenter + secondHandLength * sin(second * (2 * pi / 60))
        ySecond = yCenter - secondHandLength * cos(second * (2 * pi / 60))
        self.create_line(xCenter, yCenter, xSecond, ySecond, fill = "red", tags = "clock")

        minute = self.__minute
        xMinute = xCenter + minuteHandLength * sin(minute * (2 * pi / 60))
        yMinute = yCenter - minuteHandLength * cos(minute * (2 * pi / 60))
        self.create_line(xCenter, yCenter, xMinute, yMinute, fill = "blue", tags = "clock")

        hour = self.__hour
        xHour = xCenter + hourHandLength * sin((hour + minute / 60) * (2 * pi / 12))
        yHour = yCenter - hourHandLength * cos((hour + minute / 60) * (2 * pi / 12))
        self.create_line(xCenter, yCenter, xHour, yHour, fill = "green", tags = "clock")

        timestr  = f"{str(hour)}:{str(minute)}:{str(second)}"
        self.create_text(width / 2, height / 2 + radius + 10, text = timestr, tags = "clock")
