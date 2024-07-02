from tkinter import *

root = Tk()

# Create a label widget
myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="It's ya boy")
# shove it onto the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

root.mainloop()
