import tkinter as tk
import webbrowser


def LmaoGetSiked():
	webbrowser.webbrowser("https://www.youtube.com/watch?v=zEpB4aNHllA")



root = tk.Tk()

#Tk() is a speical method called a constructor, which is a special method only called once and it sets everything up.

lab = tk.Label(root, text="Pick the number of chromosomes to put in the bag")

lab.grid(row = 0, column = 0)


ent = tk.Entry (root)
ent.grid(row =1, column = 0)

btn = tk.Button(root, text = "Submit", command="LmaoGetSiked")
btn.grid(row = 2, column = 0)


output = tk.Text(root, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
output.config(state = "disabled")
output.grid(row = 0, column = 1, rowspan = 3)




root.mainloop()