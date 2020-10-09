# Noah Cousino
# R01506332

##############
# Question 1 #
##############
# Make a Rectangle

# import tkinter
from tkinter import Tk, Frame, Canvas, StringVar, IntVar, Radiobutton, Checkbutton

class shapes:
    def __init__(self):
        # make the window
        window = Tk()
        window.title("Draw Shapes")

        # make two frames
        frameCan = Frame(window)
        frameBtn = Frame(window)
        frameCan.pack()
        frameBtn.pack()

        # make the canvas
        self.canvas = Canvas(frameCan, width=200, height=150)
        self.canvas.pack()

        # make the buttons and vars
        self.shape = StringVar()
        self.fill = IntVar()
        rdbRect = Radiobutton(frameBtn, text = "Rectangle", variable = self.shape, value = "r", command = self.draw).grid(row=1, column=1)
        rdbOval = Radiobutton(frameBtn, text = "Oval", variable = self.shape, value = "o", command = self.draw).grid(row=1, column=2)
        cbtFill = Checkbutton(frameBtn, text = "Fill", variable = self.fill, command = self.draw).grid(row=1, column=3)

        # window loop
        window.mainloop()

    def draw(self):
        # erase everything
        self.canvas.create_rectangle(0,0,200,150, outline = "white", fill="white")

        # draw what is there
        if self.shape.get() == "r":
            if self.fill.get() == 1:
                self.canvas.create_rectangle(10, 10, 190, 140, fill="black")
            else:
                self.canvas.create_rectangle(10, 10, 190, 140)
        elif self.shape.get() == "o":
            if self.fill.get() == 1:
                self.canvas.create_oval(10, 10, 190, 140, fill="black")
            else:
                self.canvas.create_oval(10, 10, 190, 140)

shapes()
