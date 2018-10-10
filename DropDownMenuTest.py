import tkinter as tk
from tkinter import *


# the constructor syntax is:
# OptionMenu(master, variable, *values)

OPTIONS = [
    "Convert lb to kg",
    "Calculate Calories Burnt",
    "Calculate Pace"
]

master = Tk()

variable = StringVar(master)
variable.set(OPTIONS[0]) # default value

w = apply(OptionMenu, (master, variable) + tuple(OPTIONS))
w.pack()

mainloop()