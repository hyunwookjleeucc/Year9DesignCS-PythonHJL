import tkinter as tk

root = tk.Tk()

labwp = tk.Label(root, text="Enter weight in lb")
labwp.grid()

entwp = tk.Entry(root)
entwp.pack()

btn1 = tk.Button(root, text="Convert", command=convert)
btn1.pack()

output1 = tk.Text(root, width=35, height=4, borderwidth=3, relief=tk.GROOVE)
output1.config(state="disabled")
output1.pack()



root.mainloop()