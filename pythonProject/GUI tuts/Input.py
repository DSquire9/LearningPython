from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()

def myClick():
        myLabel = Label(root, text=e.get())
        myLabel.pack()


myButton = Button(root, text="Click Me!", padx=50, pady=50, command=myClick, fg="blue", bg="green")
myButton.pack()


root.mainloop()
