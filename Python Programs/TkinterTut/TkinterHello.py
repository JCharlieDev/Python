from tkinter import *
#   Mostly everything is a widget

#   Main Window
root = Tk()
#   Creating label widget
myLabel = Label(root, text = "Hello world")
#   Putting it on the screen
myLabel.pack()

#   Event loop, loops the application to stay open

root.mainloop()