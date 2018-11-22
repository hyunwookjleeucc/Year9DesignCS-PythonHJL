import tkinter as tk

class WeightConversion():

	def __init__(self):

		#Create all data variables
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
		self.w1 = float(self.entwp.get())

		self.wkg = self.w1/2.205
		self.wkg = round(self.wkg,0)

		self.output1.config(state="normal")

		outputValue1= "Your weight in kg is: " + str(self.wkg) + "kg."


		self.output1.delete(1.0, tk.END)
		self.output1.insert (tk.INSERT, outputValue1)
		self.output1.config(state="disabled")



mainpage = WeightConversion()

#class LoginPage():

	# The first thing is always the constructor (all the code that you write now will be in the constructor)
	# Type two underscores before typing init and two after.
	#def __init__(self):
		#print("Running Constructor")
		#all variables are to be instance variables.
		#self.root = tk.Tk()
		#self.labu = tk.Label(self.root, text= "username")
		#self.labu.pack()
#ordered parameters: The order we send them matters. (COMMON)
#named parameters: JavaScript and Python specific

		#self.entu = tk.Entry(self.root)
		#self.entu.pack()

		#self.labp = tk.Label(self.root, text= "password")
		#self.labp.pack()

		#self.entp = tk.Entry(self.root, show = "*")
		#self.entp.pack()

		#self.btnl = tk.Button(self.root, text="Submit", command = self.clicked)
		#self.btnl.pack()

		#self.root.mainloop()

	#def clicked(self):
			#print("clicked")


#mainpage = LoginPage()