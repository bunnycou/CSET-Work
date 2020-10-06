##############
# Question 5 #
##############
# GUI Loan Calculator

from tkinter import Tk, Label, Entry, Button, StringVar, RIGHT, W, E

class LoanCalculatoor:
    def __init__(self):
        window = Tk()
        window.title("Loan Calculator")

        Label(window, text = "Annual Interest Rate").grid(row = 1, column = 1, sticky = W)
        Label(window, text = "Number of Years").grid(row = 2, column = 1, sticky = W)
        Label(window, text = "Loan Amount").grid(row = 3, column = 1, sticky = W)
        Label(window, text = "Monthly Payment").grid(row = 4, column = 1, sticky = W)
        Label(window, text = "Total Payment").grid(row = 5, column = 1, sticky = W)

        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable = self.annualInterestRateVar, justify = RIGHT).grid(row = 1, column = 2)
        
        self.numberofYearsVar = StringVar()
        Entry(window, textvariable = self.numberofYearsVar, justify = RIGHT).grid(row = 2, column = 2)
        
        self.loanAmountVar = StringVar()
        Entry(window, textvariable = self.loanAmountVar, justify = RIGHT).grid(row = 3, column = 2)
        
        self.monthlyPaymentVar = StringVar()
        lblMonthlyPayment = Label(window, textvariable = self.monthlyPaymentVar).grid(row = 4, column = 2, sticky = E)

        self.totalPaymentVar = StringVar()
        lblTotalPayment = Label(window, textvariable = self.totalPaymentVar).grid(row = 5, column = 2, sticky = E)

        btbComputePayment = Button(window, text = "Compute Payment", command = self.computePayment).grid(row = 6, column = 2, sticky = E)

        window.mainloop()

    def computePayment(self):
        monthlyPayment = self.getmonthlyPayment(float(self.loanAmountVar.get()), float(self.annualInterestRateVar.get()) / 1200, int(self.numberofYearsVar.get()))
        self.monthlyPaymentVar.set(format(monthlyPayment, "10.2f"))
        totalPayment = float(self.monthlyPaymentVar.get()) * 12 * int(self.numberofYearsVar.get())
        self.totalPaymentVar.set(format(totalPayment, "10.2f"))

    def getmonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):
        monthlyPayment = loanAmount * monthlyInterestRate / ( 1 - 1 / (1+ monthlyInterestRate) ** (numberOfYears * 12))
        return monthlyPayment

LoanCalculatoor()


