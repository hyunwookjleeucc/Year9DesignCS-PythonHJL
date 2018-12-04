import tkinter as tk
from tkinter import ttk
import subprocess
import threading
import webbrowser as web
import os


def convert():
	try:
		w1 = float(entwp.get())

		wkg = w1/2.205
		wkg = round(wkg,0)

		output1.config(state="normal")

		outputValue1= "Your weight in kg is: " + str(wkg) + "kg."


		output1.delete(1.0, tk.END)
		output1.insert (tk.INSERT, outputValue1)
		output1.config(state="disabled")
	except ValueError:
		output1.config(state="normal")
		output1.delete(1.0, tk.END)
		output1.insert (tk.INSERT, "INVALID")
		output1.config(state="disabled")


def calculate():


	try:
		w = float(entw.get())
		t = float(entt.get())
		i = float(enti.get())


		c = ((w*i*3.5)/200)*t
		c = round(c,2)

		output.config(state="normal")

		outputValue= "Given\nweight:" +str(w) + " kg\ntime:" +str(t) + " minutes\nintensity:" +str(i) + "\nThe calories you burned today is " + str(c) + " kcal."


		output.delete(1.0, tk.END)
		output.insert (tk.INSERT, outputValue)
		output.config(state="disabled")
		
		f = open("swimreccordss.txt", "a")
		f.write(str(c) + "kcal" + "\n")
		f.close()
	except ValueError:
		output.config(state="normal")
		output.delete(1.0, tk.END)
		output.insert (tk.INSERT, "INVALID")
		output.config(state="disabled")

def calculatep():

	try:
		d = float(entd.get())
		t1 = float(ent1.get())

		p = d/t1
		p = round(p,2)

		output2.config(state="normal")

		outputValue2= "Given\ndistance:" + str(d) + " yards\ntime:" + str(t1) + " minutes\nYour pace is " + str(p) + " yards per minute."

		output2.delete(1.0, tk.END)
		output2.insert (tk.INSERT, outputValue2)
		output2.config(state="disabled")
		
		f = open("swimreccords_pace.txt", "a")
		f.write(str(p) + "yards per minute" + "\n")
		f.close()
	except ValueError:
		output2.config(state="normal")
		output2.delete(1.0, tk.END)
		output2.insert (tk.INSERT, "INVALID")
		output2.config(state="disabled")

def say(text):
	subprocess.call(['say', text])

def runSpeechprep(*args):
	t = threading.Thread(target=runSpeech)
	t.start()
    
def runSpeech(*args):
	os.system("say \"This program will calculate the calories you burnt and your pace using accurate calculations. Enter your weight, the time you swam, the intensity of the swim, and the distance\"")
	os.system("say \"To figure out the calories you burnt and the pace you swam at. This program is made to help you keep track of your siwm throughout the season and improve and prepare for OFSAA\"")
	os.system("say \"I hope you like my program and you can give me feedback on my website, https://sites.google.com/ucc.on.ca/year9designcoding-hjlee/unit-1/developing-ideas. The link will be below.\"")

def transport():
	web.open("https://sites.google.com/ucc.on.ca/year9designcoding-hjlee/unit-1/developing-ideas")

def onclick(btnStop):
	Break(runSpeech)

root = tk.Tk()
root.title("Complete Swimmer Calculator")
root.config(bg= "#19535F")

tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="Weight")
tabControl.grid()

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Calories")
tabControl.grid()

tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text="Pace")
tabControl.grid()


#***********************************************************Converting lb into kg***********************************************************
labwp = tk.Label(tab1, text="Enter weight here in lb to find out weight in kg")
labwp.config(bg = "#D7C9AA")
labwp.grid(row = 0 , column = 0)

entwp = tk.Entry(tab1)
entwp.grid(row = 1, column = 0)

btn1 = tk.Button(tab1, text="Convert", command=convert)
btn1.config(highlightbackground = "#D7C9AA")
btn1.grid(row = 2, column = 0)

output1 = tk.Text(tab1, width=35, height=4, borderwidth=3, relief=tk.GROOVE)
output1.config(state="disabled")
output1.grid(row = 3, column = 0, rowspan= 2)

logo = tk.PhotoImage(file = "LogoMakr_34UUHt.png")
logoImage = tk.Label(image = logo)
logoImage.config(bg = "#19535F")
logoImage.grid(row = 0, column = 1, rowspan = 9)

#***********************************************************Accessibility Options******************************************************************
btnAccess = tk.Button(text="Text-to-speech", command = runSpeechprep)
btnAccess.config(highlightbackground = "#D7C9AA")
btnAccess.grid(row = 2, column = 0, sticky = "NEWS")

btnAccess2 = tk.Button(text="Contrast Colours")
btnAccess2.config(highlightbackground = "#D7C9AA")
btnAccess2.grid(row = 4, column = 0, sticky = "NEWS")

btnAccess3 = tk.Button(text="Increase Font")
btnAccess3.config(highlightbackground = "#D7C9AA")
btnAccess3.grid(row = 5, column = 0, sticky = "NEWS")

btnStop = tk.Button(text="Stop Text-to-speech", command = onclick)
btnStop.config(highlightbackground = "#D7C9AA")
btnStop.grid(row = 3, column = 0, sticky = "NEWS")

#***********************************************************Link to Website***********************************************************
btnWebsite = tk.Button(text="My website", command = transport)
btnWebsite.config(highlightbackground = "#D7C9AA")
btnWebsite.grid(row = 6, column = 0, sticky = "NEWS")

#***********************************************************Calculating Calories Burnt***********************************************************
labw = tk.Label(tab2, text="Enter weight in kg")
labw.config(bg = "#D7C9AA")
labw.grid(row = 5, column = 0)

entw = tk.Entry(tab2)
entw.grid(row = 6, column = 0, sticky = "N")

labt = tk.Label(tab2, text="How long did you swim today?(in minutes)")
labt.config(bg = "#D7C9AA")
labt.grid(row = 7, column = 0, sticky = "N")

entt = tk.Entry(tab2)
entt.grid(row = 8, column = 0, sticky = "N")

labi = tk.Label(tab2, text="How intense was the swim today?" + "\n(Leisure= 6, Moderate= 8, Intense= 9, Full-Out= 11)")
labi.config(bg = "#D7C9AA")
labi.grid(row =9, column = 0, sticky = "N")

enti = tk.Entry(tab2)
enti.grid(row = 10, column = 0, sticky = "N")

btn = tk.Button(tab2, text="Calculate calories burnt", command=calculate)
btn.config(highlightbackground = "#D7C9AA")
btn.grid(row = 11, column = 0, sticky = "N")


output = tk.Text(tab2, width=50, height=15, borderwidth=3, relief=tk.GROOVE)
output.config(state="disabled")
output.grid(row = 12, column = 0, rowspan= 2, sticky = "N")

#***********************************************************Calculating the Pace***********************************************************

labd = tk.Label(tab3, text="How many yards did you swim today? (One length of UCC pool is 20yards)")
labd.config(bg = "#D7C9AA")
labd.grid(row = 0, column = 1)

entd = tk.Entry(tab3)
entd.grid(row = 1, column = 1)

labt1 = tk.Label(tab3, text="How long did you swim today?(in minutes)")
labt1.config(bg = "#D7C9AA")
labt1.grid(row = 2, column = 1,)

ent1 = tk.Entry(tab3)
ent1.grid(row = 3, column = 1, sticky = "N")

btn2 = tk.Button(tab3, text="Calculate Pace", command=calculatep)
btn2.config(highlightbackground = "#D7C9AA")
btn2.grid(row = 4, column = 1)

output2 = tk.Text(tab3, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
output2.config(state="disabled")
output2.grid(row = 5, column = 1)


root.mainloop()