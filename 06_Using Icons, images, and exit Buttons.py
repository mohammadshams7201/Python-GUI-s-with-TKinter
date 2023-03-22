# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 21:21:09 2023

@author: Mohammad  Shams
"""

from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("TKinter with Mohammad")

root.iconbitmap('icon.ico')

my_img = ImageTk.PhotoImage(Image.open("gray.jpeg"))
my_label = Label(image=my_img)
my_label.pack()





buttons_quit = Button(root, text="Exit Program", command = root.quit)
buttons_quit.pack()





root.mainloop()