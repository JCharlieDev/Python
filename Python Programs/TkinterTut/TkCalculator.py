from tkinter import *

root = Tk()
#   Sets the title of the window
root.title("Simple Calculator")


entry = Entry(root, width = 35, borderwidth = 5)

entry.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

def ButtonClick(number):

    #   entry.delete(0, END)
    currentNumber = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(currentNumber) + str(number))

def ButtonClear():

    entry.delete(0, END)

def ButtonAddition():

    firstNumber = entry.get()
    global fNumber
    global math
    math = "addition"
    fNumber = int(firstNumber)
    entry.delete(0, END)

def ButtonSubtract():
    firstNumber = entry.get()
    global fNumber
    global math
    math = "subtraction"
    fNumber = int(firstNumber)
    entry.delete(0, END)

def ButtonMultiply():
    firstNumber = entry.get()
    global fNumber
    global math
    math = "multiply"
    fNumber = int(firstNumber)
    entry.delete(0, END)

def ButtonDivision():
    firstNumber = entry.get()
    global fNumber
    global math
    math = "division"
    fNumber = int(firstNumber)
    entry.delete(0, END)

def ButtonEqual():

    secondNumber = entry.get()

    entry.delete(0, END)

    if math == "addition":
        entry.insert(0, fNumber + int(secondNumber))

    if math == "subtraction":
        entry.insert(0, fNumber - int(secondNumber))

    if math == "multiplication":
        entry.insert(0, fNumber * int(secondNumber))

    if math == "division":
        entry.insert(0, fNumber / int(secondNumber))

#   Button define
button1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda : ButtonClick(1))
button2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda : ButtonClick(2))
button3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda : ButtonClick(3))
button4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda : ButtonClick(4))
button5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda : ButtonClick(5))
button6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda : ButtonClick(6))
button7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda : ButtonClick(7))
button8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda : ButtonClick(8))
button9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda : ButtonClick(9))
button0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda : ButtonClick(0))
buttonAdd = Button(root, text = "+", padx = 40, pady = 20, command = lambda : ButtonAddition())
buttonEqual = Button(root, text = "=", padx = 91, pady = 20, command = lambda : ButtonEqual())
buttonClear = Button(root, text = "Clr", padx = 79, pady = 20, command = lambda : ButtonClear())
buttonSubtract = Button(root, text = "-", padx = 40, pady = 20, command = lambda : ButtonSubtract())
buttonMultiply = Button(root, text = "*", padx = 40, pady = 20, command = lambda : ButtonMultiply())
buttonDivision = Button(root, text = "/", padx = 40, pady = 20, command = lambda : ButtonDivision())

#   Buttons on screen

button1.grid(row = 3, column = 0)
button2.grid(row = 3, column = 1)
button3.grid(row = 3, column = 2)

button4.grid(row = 2, column = 0)
button5.grid(row = 2, column = 1)
button6.grid(row = 2, column = 2)

button7.grid(row = 1, column = 0)
button8.grid(row = 1, column = 1)
button9.grid(row = 1, column = 2)

button0.grid(row = 4, column = 0)

buttonAdd.grid(row = 5, column = 0)
buttonClear.grid(row = 4, column = 1, columnspan = 2)
buttonEqual.grid(row = 5, column =1, columnspan = 2)

buttonSubtract.grid(row = 6, column = 0)
buttonMultiply.grid(row = 6, column = 1)
buttonDivision.grid(row = 6, column = 2)

root.mainloop()