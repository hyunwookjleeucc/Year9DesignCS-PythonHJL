import tkinter as tk
import math
import os
import webbrowser

def calculate():

	try:
		w = float(entw.get())
		t = float(entt.get())

		c = 






root = tk.Tk()
root.title = ("Become a Better Swimmer")

labw = tk.Label(root, text="Enter weight in kg: ")
labw.pack()

entw = tk.Entry(root)
entw.pack()

labt = tk.Label(root, text="How long did you swim today?")
labt.pack()

entt = tk.Entry(root)
entt.pack()

labi = tk.Label(root, text="How intense was the swim today?")
labi.pack()

enti = tk.Entry(root)
enti.pack()

btn = tk.Button(root, text="Calculate calories burnt", command=calculate)
btn.pack()


output = tk.Text(root, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
output.config("disabled")
output.pack


root.mainloop()