import tkinter as tk

class PaceCalculation():

	def __init__(self):

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



mainpage = PaceCalculation()