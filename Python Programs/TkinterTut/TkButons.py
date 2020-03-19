from tkinter import *

root = Tk()

def MyClick():
    myLabel = Label(root, text = "Look I clicked a button!")
    myLabel.pack()

#   Button Properties: State (Disabled)
#   padx = float    -   setx de x dimension
#   pady = float    -   setx de y dimension

#   Functions don't need the parenthesis
myButton = Button(root, text = "Click me!", padx = 50, pady = 50, command = MyClick)
myButton.pack()



root.mainloop()
