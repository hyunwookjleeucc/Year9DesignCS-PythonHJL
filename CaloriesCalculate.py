import tkinter as tk

class CalculateCalories():

	def __init__(self):

		#Create all data variables
		self.w = 0
		self.t = 0
		self.i = 0
		self.c = 0

		print("Running Constructor")

		self.root = tk.Tk()

		self.labw = tk.Label(self.root, text="Enter weight in kg")
		self.labw.grid(row = 0, column = 0)

		self.entw = tk.Entry(self.root)
		self.entw.grid(row = 1, column = 0)

		self.labt = tk.Label(self.root, text="How long did you swim today?(in minutes)")
		self.labt.grid(row = 2 , column = 0)

		self.entt = tk.Entry(self.root)
		self.entt.grid(row = 3, column = 0)

		self.labi = tk.Label(self.root, text="How intense was the swim today?" + "\n(Leisure= 6, Moderate= 8, Intense= 9, Full-Out= 11)")
		self.labi.grid(row = 1, column = 1)

		self.enti = tk.Entry(self.root)
		self.enti.grid(row = 2, column = 1)

		self.btn = tk.Button(self.root, text="Calculate calories burnt", command=self.calculate)
		self.btn.grid(row = 3, column = 1, columnspan = 2)


		self.output = tk.Text(self.root, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
		self.output.config(state="disabled")
		self.output.grid(row = 4, column = 0, columnspan = 2)

		self.root.mainloop()

	def calculate(self):
	try:
		self.w = float(self.entw.get())
		self.t = float(self.entt.get())
		self.i = float(self.enti.get())

		self.c = ((self.w*self.i*3.5)/200)*self.t
		self.c = round(self.c,2)

		self.output.config(state="normal")

		outputValue= "Given\nweight:" +str(self.w) + " kg\ntime:" +str(self.t) + " minutes\nintensity:" +str(self.i) + "\nThe calories you burned today is " + str(self.c) + " kcal."


		self.output.delete(1.0, tk.END)
		self.output.insert (tk.INSERT, outputValue)
		self.output.config(state="disabled")

	except ValueError:
		self.output.config(state="normal")
		self.output.delete(1.0, tk.END)
		self.output.insert (tk.INSERT, "INVALID")
		self.output.config(state="disabled")


mainpage = CalculateCalories()
