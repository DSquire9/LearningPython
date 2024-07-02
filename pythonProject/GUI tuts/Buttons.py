from tkinter import *

root = Tk()

def myClick():
        myLabel = Label(root, text="Button Clicked")
        myLabel.pack()


myButton = Button(root, text="Click Me!", padx=50, pady=50, command=myClick, fg="blue", bg="green")
myButton.pack()


root.mainloop()
