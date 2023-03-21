# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 01:02:13 2023

@author: Mohammad  Shams
"""

from tkinter import *

root = Tk()


#Creating a label Widget
myLabel1 = Label(root, text = "Hey there !")
myLabel2 = Label(root, text = "I am Mohammad Shams")
myLabel3 = Label(root, text = "a P.h.D student")

#Showing it onto the screen
myLabel1.grid(row=0, column=1)
myLabel2.grid(row=1, column=5)
myLabel3.grid(row=2, column=1)

root.mainloop()

