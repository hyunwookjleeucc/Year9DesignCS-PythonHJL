import tkinter as tk
import os
import webbrowser


def convert():
	try:
		w1 = float(entwp.get())

		wkg = w1/2.205
		wkg = round(wkg,0)

		output1.config(state="normal")

		outputValue1= "Your weight in kg is: " + str(wkg) + "kg."


		output1.delete(1.0, tk.END)
		output1.insert (tk.INSERT, outputValue1)
		output1.config(state="disabled")
	except ValueError:
		output1.config(state="normal")
		output1.delete(1.0, tk.END)
		output1.insert (tk.INSERT, "INVALID")
		output1.config(state="disabled")


def calculate():


	try:
		w = float(entw.get())
		t = float(entt.get())
		i = float(enti.get())


		c = ((w*i*3.5)/200)*t
		c = round(c,2)

		output.config(state="normal")

		outputValue= "Given\nweight:" +str(w) + " kg\ntime:" +str(t) + " minutes\nintensity:" +str(i) + "\nThe calories you burned today is " + str(c) + " kcal."


		output.delete(1.0, tk.END)
		output.insert (tk.INSERT, outputValue)
		output.config(state="disabled")
		
		f = open("swimreccordss.txt", "a")
		f.write(str(c) + "\n")
		f.close()
	except ValueError:
		output.config(state="normal")
		output.delete(1.0, tk.END)
		output.insert (tk.INSERT, "INVALID")
		output.config(state="disabled")

def calculatep():

	try:
		d = float(entd.get())
		t1 = float(ent1.get())

		p = d/t1
		p = round(p,2)

		output2.config(state="normal")

		outputValue2= "Given\ndistance:" + str(d) + " yards\ntime:" + str(t1) + " minutes\nYour pace is " + str(p) + " yards per minute."

		output2.delete(1.0, tk.END)
		output2.insert (tk.INSERT, outputValue2)
		output2.config(state="disabled")
		
		f = open("swimreccords_pace.txt", "a")
		f.write(str(p) + "\n")
		f.close()
	except ValueError:
		output2.config(state="normal")
		output2.delete(1.0, tk.END)
		output2.insert (tk.INSERT, "INVALID")
		output2.config(state="disabled")


root = tk.Tk()
root.title("Complete Swimmer Calculator")


#Converting lb into kg
labwp = tk.Label(root, text="Enter weight here in lb to find out weight in kg")
labwp.pack()

entwp = tk.Entry(root)
entwp.pack()

btn1 = tk.Button(root, text="Convert", command=convert)
btn1.pack()

output1 = tk.Text(root, width=35, height=4, borderwidth=3, relief=tk.GROOVE)
output1.config(state="disabled")
output1.pack()

#Calculating Calories Burnt
labw = tk.Label(root, text="Enter weight in kg")
labw.pack()

entw = tk.Entry(root)
entw.pack()

labt = tk.Label(root, text="How long did you swim today?(in minutes)")
labt.pack()

entt = tk.Entry(root)
entt.pack()

labi = tk.Label(root, text="How intense was the swim today? (Leisure= 6, Moderate= 8, Intense= 9, Full-Out= 11)")
labi.pack()

enti = tk.Entry(root)
enti.pack()

btn = tk.Button(root, text="Calculate calories burnt", command=calculate)
btn.pack()


output = tk.Text(root, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
output.config(state="disabled")
output.pack()

#Calculating the Pace

labd = tk.Label(root, text="How many yards did you swim today? (One length of UCC pool is 20yards)")
labd.pack()

entd = tk.Entry(root)
entd.pack()

labt1 = tk.Label(root, text="How long did you swim today?(in minutes)")
labt1.pack()

ent1 = tk.Entry(root)
ent1.pack()

btn2 = tk.Button(root, text="Calculate Pace", command=calculatep)
btn2.pack()

output2 = tk.Text(root, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
output2.config(state="disabled")
output2.pack()

root.mainloop()

