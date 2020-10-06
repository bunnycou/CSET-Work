##############
# Question 4 #
##############
# Program that shows how to use the canvas widget

# import tkinter
from tkinter import Tk, Button

class processButtonEvent:
    def __init__(self):

        # create the window
        window = Tk()

        # create widgets
        btOK = Button(window, text = "OK", fg = "red", command = self.processOK)
        btCancel = Button(window, text = "Cancel", bg = "Yellow", command = self.processCancel)
        
        # place widgets
        btOK.pack()
        btCancel.pack()

        # loop event
        window.mainloop()

    def processOK(self):
        print("OK Button is Clicked")

    def processCancel(self):
        print("Cancel Button is Clicked")

processButtonEvent()
