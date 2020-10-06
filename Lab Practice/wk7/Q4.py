##############
# Question 4 #
##############
# Program that shows how to use the canvas widget

from tkinter import *

class CavasDemo:
    def __init__(self):
        window = Tk()
        window.title("Canvas Demo")

        frame1 = Frame(window)
        frame1.pack()

        canvas = Canvas(frame1, bg = "white", height = 300, width = 300)
        rect = canvas.create_rectangle(10, 10, 30, 20)

        canvas.pack()
        window.mainloop()

CanvasDemo()
