# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 01:36:46 2023

@author: Mohammad  Shams
"""

from tkinter import *

root = Tk()
e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter your name: ")

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


myButton = Button(root, text="Enter your name", command=myClick, fg="blue", bg="orange")

myButton.pack()

root.mainloop()
