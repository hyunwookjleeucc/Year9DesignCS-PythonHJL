import tkinter as tk
import math


def calculate():

	r = float(entr.get())
	h = float(enth.get())

	v = math.pi*r*r*h/3
	v = round(v,2)

	output.config(state="normal")

	outputValue= "Given\nradius:" +str(r) + " units\nheight:" +str(h) + " units\nThe volume is " + str(v) + " units cubed."


	output.delete(1.0, tk.END)
	output.insert (tk.INSERT, outputValue)
	output.config(state="disabled")


root = tk.Tk()
root.title("Volume of a Circular Cone")


labr = tk.Label(root, text="radius")
labr.pack()

entr = tk.Entry(root)
entr.pack()

labh = tk.Label(root, text = "height")
labh.pack()

enth = tk.Entry(root)
enth.pack()


btn = tk.Button(root, text="Calculate", command=calculate)
btn.pack()

output = tk.Text(root, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
output.config(state="disabled")
output.pack()





f = open("calculations.txt", "w")
f.write(int(v) + "\n")

f.close()

root.mainloop()


















