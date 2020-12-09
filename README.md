# Python Tutorial (Login System)

In this tutorial, we will learn how to create login system by writing some Python GUI examples using the
Tkinter package.

Tkinter package is shipped with Python as a standard package, so we don’t need to install anything to use it.



#### You need to have:
* Python 3.9.
* IDE
* Tkinter, random, os libraries
* Creativity

## Getting Started
First, we will import Tkinter package and create a window and set its title:
from tkinter import *
from random import choice
import os

root = Tk()
root.resizable(False, False)
root.title("Sign In")
root.geometry("265x520+600+100")
root.iconbitmap("b.ico")
root.configure(bg="#3285a8")


root.mainloop()


