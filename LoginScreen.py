#This imports the tkinter which contains all the support material t omake GUI elements and as tk
#means that it is a short name to use.
import tkinter as tk

root = tk.Tk() #main window
#Tk() is a special function called a CONSTRUCTOR. If a function is written with a capital letter, this indicates that it is a constructor.


labu = tk.Label(root, text= "username")
labu.pack()
#ordered parameters: The order we send them matters. (COMMON)
#named parameters: JavaScript and Python specific

entu = tk.Entry(root)
entu.pack(padx = 10)

labp = tk.Label(root, text= "password")
labp.pack()

entp = tk.Entry(root, show = "*")
entp.pack()

btnl = tk.Button(root, text="Submit")
btnl.pack()

root.mainloop()