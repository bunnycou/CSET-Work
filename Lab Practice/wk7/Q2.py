##############
# Question 2 #
##############
# Example of a program that uses the widgets

# import tkinter
from tkinter import Tk, Frame
from tkinter import Checkbutton, Radiobutton, Button, Text, Message, Label, Entry
from tkinter import IntVar, StringVar, END

class widgetsDemo:
    def __init__(self):

        # create the window
        window = Tk()
        window.title("Widget Demo")

        # create the first frame
        frame1 = Frame(window)
        frame1.pack()

        # create variables for buttons and create the buttons
        self.v1 = IntVar()
        cbtBold = Checkbutton(frame1, text = "Bold", variable = self.v1, command = self.processCheckbutton)
        self.v2 = IntVar()
        rbRed = Radiobutton(frame1, text = "Red", bg = "red", variable = self.v2, value = 1, command = self.processRadiobutton)
        rbYellow = Radiobutton(frame1, text = "Yellow", bg = "yellow", variable = self.v2, value = 2, command = self.processRadiobutton)
        
        # set the buttons in the frame
        cbtBold.grid(row = 1, column = 1)
        rbRed.grid(row = 1, column = 2)
        rbYellow.grid(row = 1, column = 3)

        # create the second frame
        frame2 = Frame(window)
        frame2.pack()

        # create labels and entry and button and message
        label = Label(frame2, text = "Enter Your Name: ")
        self.name = StringVar()
        entryName = Entry(frame2, textvariable = self.name)
        btGetName = Button(frame2, text = "Get Name", command = self.processButton)
        message = Message(frame2, text = "This is the Message Widget")

        # position what we just made
        label.grid(row = 1, column = 1)
        entryName.grid(row = 1, column = 2)
        btGetName.grid(row = 1, column = 3)
        message.grid(row = 1, column = 4)

        # create a text window and add text to it
        text = Text(window)
        text.pack()
        text.insert(END, "Tip\nThe Best way to learn tkinter is to read ")
        text.insert(END, "these carefully designed examples and use them ")
        text.insert(END, "to create your application")

        window.mainloop()

    # functions for processing button clicks
    def processCheckbutton(self):
        print(f"check button is {'checked' if self.v1.get() == 1 else 'unchecked'}")

    def processRadiobutton(self):
        print(f"{'Red' if self.v2.get() == 1 else 'Yellow'} is selected")

    def processButton(self):
        print(f"Your name is {self.name}")

# run everything
widgetsDemo()
