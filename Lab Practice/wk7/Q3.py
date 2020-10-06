##############
# Question 3 #
##############
# Program that lets the user change the color, font, and text of a label

from tkinter import Tk, Frame
from tkinter import Button, Radiobutton, Label, Entry
from tkinter import StringVar, IntVar

class ChangeLabelDemo:
    def __init__(self):
        # create the window
        window = Tk()
        window.title("Change Label Demo")

        # create the first frame
        frame1 = Frame(window)
        frame1.pack()

        # variable
        self.text = StringVar()
        self.color = IntVar()

        # create and place widget
        self.labelEdit = Label(frame1, text = "Placeholder")
        self.labelEdit.pack()

        # create the second frame
        frame2 = Frame(window)
        frame2.pack()

        # create widgets
        labelPrompt = Label(frame2, text = "Enter Text: ")
        userEntry = Entry(frame2, textvariable = self.text)
        btnChange = Button(frame2, text = "Change Text", command = self.processButton)
        rbRed = Radiobutton(frame2, text = "Red", bg = "red", variable = self.color, value = 1, command = self.processRadiobutton)
        rbYellow = Radiobutton(frame2, text = "Yellow", bg = "yellow", variable = self.color, value = 2, command = self.processRadiobutton)

        # place widgets
        labelPrompt.grid(row = 1, column = 1)
        userEntry.grid(row = 1, column = 2)
        btnChange.grid(row = 1, column = 3)
        rbRed.grid(row = 1, column = 4)
        rbYellow.grid(row = 1, column = 5)

        window.mainloop()
        
    # create functions for processing info
    def processButton(self):
        print(f"Button is clicked, text is {self.text.get()}")
        self.labelEdit["text"] = self.text.get()

    def processRadiobutton(self):
        print(f"{'Red' if self.color.get() == 1 else 'Yellow'} is selected")
        if self.color.get() == 1:
            self.labelEdit["fg"] = "red"
        else:
            self.labelEdit["fg"] = "yellow"

ChangeLabelDemo()