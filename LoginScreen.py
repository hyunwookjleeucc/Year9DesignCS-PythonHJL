import tkinter as tk

#Classes: A blueprint to make objects.
#Object: An instance of the class.

#Three Parts
#Constructor: This is a special method only run once when we first instantiate "Make" the object.
#Attributes: These are variables that describe the state of the object.
#Behaviours: These are functions that can be called that deal with the object.


class LoginPage():

	# The first thing is always the constructor (all the code that you write now will be in the constructor)
	# Type two underscores before typing init and two after.
	def __init__(self):
		print("Running Constructor")
		#all variables are to be instance variables.
		self.root = tk.Tk()
		self.labu = tk.Label(self.root, text= "username")
		self.labu.pack()
#ordered parameters: The order we send them matters. (COMMON)
#named parameters: JavaScript and Python specific

		self.entu = tk.Entry(self.root)
		self.entu.pack()

		self.labp = tk.Label(self.root, text= "password")
		self.labp.pack()

		self.entp = tk.Entry(self.root, show = "*")
		self.entp.pack()

		self.btnl = tk.Button(self.root, text="Submit", command = self.clicked)
		self.btnl.pack()


		self.root.mainloop()

	def clicked(self):
			print("clicked")


mainpage = LoginPage() #Creates an instance of the class