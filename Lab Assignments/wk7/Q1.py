# Noah Cousino
# R01506332

##############
# Question 1 #
##############
# Move a ball

#import tkinter
from tkinter import Tk, Frame, Canvas, Button

class ballMove:
    def __init__(self):
        # create base window
        window = Tk()
        window.title("Ball Move")

        # create necessary frames
        frameCan = Frame(window)
        frameCan.pack()

        frameBtn = Frame(window)
        frameBtn.pack()

        # make the ball and variable for coords
        self.canvas = Canvas(frameCan, bg="white", width=250,height = 150)
        self.canvas.pack()
        self.coords = [120, 70, 130, 80]
        ball = self.canvas.create_oval(self.coords, fill="black")

        # create the buttons
        btnUp = Button(frameBtn, text="Up", command=self.up)
        btnDown = Button(frameBtn, text="Down", command=self.down)
        btnLeft = Button(frameBtn, text="Left", command=self.left)
        btnRight = Button(frameBtn, text="Right", command=self.right)

        # place btns
        btnUp.grid(row=1, column=2)
        btnDown.grid(row=3, column=2)
        btnLeft.grid(row=2, column=1)
        btnRight.grid(row=2, column=3)

        # keep window open
        window.mainloop()

    def up(self):
        # erase the ball
        self.canvas.create_rectangle(self.coords, outline="white", fill="white")

        # move the ball coords
        if self.coords[1] < 10:
            pass
        else:
            self.coords[1] -= 10
            self.coords[3] -= 10

        # draw the new circle
        self.canvas.create_oval(self.coords, fill="black")

    def down(self):
        # erase the ball
        self.canvas.create_rectangle(self.coords, outline="white", fill="white")

        # move the ball coords
        if self.coords[3] > 140:
            pass
        else:
            self.coords[1] += 10
            self.coords[3] += 10

        # draw the new circle
        self.canvas.create_oval(self.coords, fill="black")

    def left(self):
        # erase the ball
        self.canvas.create_rectangle(self.coords, outline="white", fill="white")

        # move the ball coords
        if self.coords[0] < 10:
            pass
        else:
            self.coords[0] -= 10
            self.coords[2] -= 10

        # draw the new circle
        self.canvas.create_oval(self.coords, fill="black")

    def right(self):
        # erase the ball
        self.canvas.create_rectangle(self.coords, outline="white", fill="white")

        # move the ball coords
        if self.coords[2] > 240:
            pass
        else:
            self.coords[0] += 10
            self.coords[2] += 10

        # draw the new circle
        self.canvas.create_oval(self.coords, fill="black")

ballMove()
