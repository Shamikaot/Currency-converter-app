from tkinter import *
import time
from datetime import datetime

# Converts between Euros (€) and Pounds (£)

class CurrencyConverter:

    def __init__(self, master):
        master.title("Currency converter")

        # Variables for toggling between EUR and GBP
        self.dateText = StringVar()
        self.fromCurrency = StringVar()
        self.fromCurrency.set("€")
        self.toCurrency = StringVar()
        self.toCurrency.set("£")
        self.multiplier = DoubleVar()


        # Radiobutton selected value
        self.cur = DoubleVar()

        # Result value
        self.result = IntVar()
        self.result.set(0)

        # Time
        self.today = datetime.now()
        formatToday = self.today.strftime("%A, %d, %B, %Y, %H:%M:%S")
        self.dateText.set(formatToday)
        print(self.today.strftime("%A, %d, %B, %Y"))

        # Body for widgets
        content = Frame(master, padx = 100, pady = 30)
        content.grid(row = 0, column = 0)

        content.rowconfigure(2, pad = 30)
        content.rowconfigure(3, pad = 10)
        content.rowconfigure(4, pad = 30)

        header = Label(content, text = "Exchange rate at:")
        header.grid(row = 0, column = 0)
        dateLabel = Label(content, textvariable = self.dateText)
        dateLabel.grid(row = 1, column = 0)

        # Frame for user value input
        convertFrame = Frame(content, padx = 10, pady = 10, borderwidth = 1, relief = RAISED)
        convertFrame.grid(row = 2, column = 0)

        self.convertAmount = Spinbox(convertFrame, from_ = 0, to = 1000000000, justify = RIGHT, width = 12)
        self.convertAmount.grid(sticky = 'w', row = 2, column = 0)

        convertAmountLabel = Label(convertFrame, textvariable = self.fromCurrency)
        convertAmountLabel.grid(sticky = 'w', row = 2, column = 1)

        convertEquals = Label(convertFrame, text = " = ")
        convertEquals.grid(row = 2, column = 2)

        toAmount = Label(convertFrame, textvariable = self.result)
        toAmount.grid(row = 2, column = 3)

        toAmountLabel = Label(convertFrame, textvariable = self.toCurrency)
        toAmountLabel.grid(row = 2, column = 4)

        convertButton = Button(content, text = "Convert", command = self.convert)
        convertButton.grid(row = 3, column = 0)

        # Frame for radiobuttons
        radioFrame = Frame(content, padx = 10, pady = 10, relief = RAISED, borderwidth = 1)
        radioFrame.grid(row = 4, column = 0)

        radioLabel = Label(radioFrame, text = "Direction")
        radioLabel.grid(row = 0, column = 0)

        eurosButton = Radiobutton(radioFrame, text = "€ -> £", variable = self.cur, value = 0.854392253, command = self.locale)
        eurosButton.grid(row = 1, column = 0)

        poundsButton = Radiobutton(radioFrame, text = "£ -> €", variable = self.cur, value = 1.17056049, command = self.locale)
        poundsButton.grid(row = 1, column = 1)
    
    # Converts given amount with hardcoded modifiers
    def convert(self):
        getMultiplier = self.cur.get()
        self.multiplier.set(getMultiplier)
        fromValue = self.convertAmount.get()
        self.result.set(round(int(fromValue) * self.multiplier.get(),4))

    # Localizes UI depending on selected exchange
    def locale(self):
        if self.cur.get() == 0.854392253:
            self.fromCurrency.set("€")
            self.toCurrency.set("£")
            self.convert()
            formatToday = self.today.strftime("%A, %d, %B, %Y, %H:%M:%S")
            self.dateText.set(formatToday)

        if self.cur.get() == 1.17056049:
            self.fromCurrency.set("£")
            self.toCurrency.set("€")
            self.convert()
            formatToday = self.today.strftime("%A, %B, %d, %Y, %I:%M:%S %p")
            self.dateText.set(formatToday)

root = Tk()
app = CurrencyConverter(root)

root.mainloop()