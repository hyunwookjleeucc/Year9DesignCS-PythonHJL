import tkinter as tk

root = tk.Tk()

output = tk.Text(root, bg = "blue", height = 10, width = 50, font = ("Times New Roman", 30))
#output.config(state = "disable")
output.grid(row = 0, column = 0, columnspan = 2)

btn1 = tk.Button(root, bg = "red", text= "Button 1", font = ("Times New Roman", 12))
btn1.grid(row = 1, column = 0)

btn2 = tk.Button(root, bg = "red", text = "Button 2", font = ("Times New Roman", 12))
btn2.grid(row = 2, column =0)

btn3 = tk.Button(root, bg = "red", text = "Button 3", font = ("Times New Roman", 12))
btn3.grid(row =3 , column =0)




root.mainloop()