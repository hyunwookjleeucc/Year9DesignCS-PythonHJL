import tkinter as tkinter
from PIL import ImageTk, ImageTk


window = tk.Tk()
window.title("Image Example")
window.geometry("500x368")
window.config(background= 'red')

path = "SunriseForest.jpg"

img = ImaggeTk.PhotoImage(Image.open(path))

panel = tk.Label(window, image = img)

panel.pack(side = "bottom", fill = "both", expand = "yes")

window.mainloop