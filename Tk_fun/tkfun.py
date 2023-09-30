from tkinter import *
from tkinter import Label, Button

root = Tk()
# first=Label(root, text="Hello World")
# second=Label(root, text="My name is Shanti Suresh")
# first.grid(row = 0, column = 0)
# second.grid(row = 1, columns = 5)


def myClick():
    first=Label(root, text="Hello World, I am Shanti")
    second=Label(root, text="I just clicked the button!")
    first.pack()
    second.pack()
    #first.grid(row = 0, column = 0)
    # second.grid(row = 1, columns = 5)

myButton = Button(root, text="First Button)", command=myClick)
myButton.pack()
root.mainloop()