import tkinter as tk
from tkinter import *

root = Tk()


photo=PhotoImage(file="SunriseForest.jpg")
label = Label(root, image=photo)
label.pack()

root.mainloop()