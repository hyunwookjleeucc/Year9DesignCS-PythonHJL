import tkinter as tk

class SwimCalc:



	def __init__(self):
		self.w1 = 0
		self.wkg = 0
		print("Running Constructor")
		self.root = tk.Tk()
		self.labwp = tk.Label(self.root, text="Enter weight in lb")
		self.labwp.pack()

		self.entwp = tk.Entry(self.root)
		self.entwp.pack()

		self.btn1 = tk.Button(self.root, text="Convert", command = self.convert)
		self.btn1.pack()

		self.output1 = tk.Text(self.root, width=35, height=4, borderwidth=3, relief=tk.GROOVE)
		self.output1.config(state="disabled")
		self.output1.pack()

		self.root.mainloop()

	def convert(self):
		try:
			self.w1 = float(self.entwp.get())

			self.wkg = self.w1/2.205
			self.wkg = round(self.wkg,0)

			self.output1.config(state="normal")

			outputValue1= "Your weight in kg is: " + str(self.wkg) + "kg."


			self.output1.delete(1.0, tk.END)
			self.output1.insert (tk.INSERT, outputValue1)
			self.output1.config(state="disabled")
		except ValueError:
			self.output1.config(state="normal")
			self.output1.delete(1.0, tk.END)
			self.output1.insert (tk.INSERT, "INVALID")
			self.output1.config(state="disabled")




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




	

		#Create all data variables
		self.d = 0
		self.t1 = 0
		self.p = 0

		print("Running Constructor")
		self.root = tk.Tk()
		self.labd = tk.Label(self.root, text="How many yards did you swim today? (One length of UCC pool is 20yards)")
		self.labd.pack()

		self.entd = tk.Entry(self.root)
		self.entd.pack()

		self.labt1 = tk.Label(self.root, text="How long did you swim today?(in minutes)")
		self.labt1.pack()

		self.ent1 = tk.Entry(self.root)
		self.ent1.pack()

		self.btn2 = tk.Button(self.root, text="Calculate Pace", command=self.calculatep)
		self.btn2.pack()

		self.output2 = tk.Text(self.root, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
		self.output2.config(state="disabled")
		self.output2.pack()

		self.root.mainloop()

	def calculatep(self):

		try:
			self.d = float(self.entd.get())
			self.t1 = float(self.ent1.get())

			self.p = self.d/self.t1
			self.p = round(self.p,2)

			self.output2.config(state="normal")

			outputValue2= "Given\ndistance:" + str(self.d) + " yards\ntime:" + str(self.t1) + " minutes\nYour pace is " + str(self.p) + " yards per minute."

			self.output2.delete(1.0, tk.END)
			self.output2.insert (tk.INSERT, outputValue2)
			self.output2.config(state="disabled")
		
		except ValueError:
			self.output2.config(state="normal")
			self.output2.delete(1.0, tk.END)
			self.output2.insert (tk.INSERT, "INVALID")
			self.output2.config(state="disabled")


mainpage = SwimCalc()