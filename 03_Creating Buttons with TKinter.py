# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 01:17:26 2023

@author: Mohammad  Shams
"""

from tkinter import *

root = Tk()


def myClick():
    myLabel = Label(root, text="Look! I clicked a Button!!")
    myLabel.pack()


myButton = Button(root, text="Click Me!", command=myClick, fg="blue", bg="#aaaaaa")
#myButton = Button(root, text="Click Me!", command=myClick, fg="blue", bg="orange")

myButton.pack()

root.mainloop()

