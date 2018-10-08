from tkinter import messagebox

answer = messagebox.askyesno("Question","Do you want to save this file?")

if answer == "no":
	f = open("tkquestiontest.txt", "a")
	f.close()

else:
	f = open("tkquestiontest.txt", "a")
	f.write((int(14871394))
	f.close()