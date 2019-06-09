# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 15:36:57 2019

@author: user1
"""

import tkinter as tk
#from tkFileDialog   import askopenfilename
def NewFile():
    print ("New File!")
def OpenFile():
    print ("Open File!")
def About():
    print( "This is a simple example of a menu")
root = tk.Tk()
menu = tk.Menu(root)
root.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
helpmenu = tk.Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)
root.mainloop()